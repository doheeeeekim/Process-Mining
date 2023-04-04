# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:11:41 2023

@author: Dohee Kim

"""
import statistics
import pm4py
import pandas as pd
import matplotlib.pyplot as plt
from pm4py.objects.log.importer.xes import importer
from pm4py.objects.conversion.log.converter import to_data_frame
from pm4py.algo.filtering.pandas.attributes import attributes_filter
from pm4py.algo.filtering.log.timestamp import timestamp_filter
from pm4py.algo.filtering.log.end_activities import end_activities_filter
from pm4py.algo.filtering.log.start_activities import start_activities_filter
from pm4py.visualization.graphs import visualizer as graphs_visualizer
from pm4py.util import constants
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.decisiontree import visualizer as tree_visualizer
from pm4py.algo.decision_mining import algorithm as decision_mining

#데이터를 import한다.
log=importer.apply('repairExample.xes') #전화기 수리 프로세스 데이터

#이벤트로그 프린트 1. print the first trace of the event log
print(log[0])

#이벤트로그 프린트 2. print the first event of the first trace
print(log[0][0])

#데이터프레임으로 변환
df=to_data_frame.apply(log)
df.head()

##컬럼명 설정
#Case ID: case:concept:name
#Activity: concept:name
#Timestamp: time:timestamp(datetime형태)
#Resource: org:resource
#case attribute: case:컬럼명

##EDA
#Activity & Resource Analysis
#1.Activity와 resource 목록 도출
activities=attributes_filter.get_attribute_values(df, attribute_key='concept:name')
resources=attributes_filter.get_attribute_values(df, attribute_key='org:resource')
#2.activity 목록 print
print(activities)

#Activity와 Resource barchart
fig,ax=plt.subplots(nrows=1, ncols=2, figsize=(25,10))
ax=ax.ravel()
ax[0].bar(x=list(activities.keys()),height=list(activities.values()))
ax[0].set_title("Activity Distribution",fontsize=20)
ax[1].bar(x=list(resources.keys()),height=list(resources.values()))
ax[1].set_title("Resource Distribution",fontsize=20)

#Start & End Activities
#1.start activity와 End activity 목록 도출
start_activities = start_activities_filter.get_start_activities(log)
end_activities = end_activities_filter.get_end_activities(log)

#2.start activity와 end activity의 분포 barchart
fig,ax=plt.subplots(nrows=1, ncols=2, figsize=(25,10))
ax=ax.ravel()
ax[0].bar(x=list(start_activities.keys()),height=list(start_activities.values()))
ax[0].set_title("Start activity Distribution",fontsize=20)
ax[1].bar(x=list(end_activities.keys()),height=list(end_activities.values()))
ax[1].set_title("End activity Distribution",fontsize=20)

#Filtering: 필요하지 않은 데이터를 제거하는 필터링이 필수적
##기존 이벤트로그의 종료 액티비티 목록
print(end_activities)
##필터링
filtered_log=end_activities_filter.apply(log, ["Repair(Complex)"],  parameters={'positive':False})
filtered_end_activities = end_activities_filter.get_end_activities(filtered_log)
##필터링된 이벤트 로그의 종료 액티비티 목록
print(filtered_end_activities)

#Process Discovery(alphaminer)
net, initial_marking, final_marking=alpha_miner.apply(log)
#Process model visualization
gviz=pn_visualizer.apply(net,initial_marking, final_marking)
pn_visualizer.view(gviz)
#Directly followed graph(프로세스맵 도출)
##FREQUENCY: 빈도
dfg=dfg_discovery.apply(log)
gviz1=dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz1)
##PERFORMANCE: 소요시간
dfg=dfg_discovery.apply(log, variant=dfg_discovery.Variants.FREQUENCY)
gviz2=dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
dfg_visualization.view(gviz2)
##bpmn
process_tree=pm4py.discover_process_tree_inductive(log)
bpmn_model=pm4py.convert_to_bpmn(process_tree)
pm4py.view_bpmn(bpmn_model)
##Process tree
pm4py.view_process_tree(process_tree)
##Heuristic Miner
map=pm4py.discover_heuristics_net(log)
pm4py.view_heuristics_net(map)
