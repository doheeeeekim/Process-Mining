# Processmining Study
프로세스마이닝 스터디 내용 정리(전화기 수리 프로세스 데이터 사용)
## 1. Process-Mining file 불러오기, 목록도출
1) xes 파일 불러오기
2) Eventlog print
3) 데이터프레임 변환
4) 컬럼명 설정
- Case ID: case:concept:name
- Activity: concept:name
- Timestamp: time:timestamp(datetime)
- Resource: org:resource
- Case attribute: case:컬럼명
## 2. EDA
1) Activity&Resource Analysis

![Figure 2023-04-03 215429](https://user-images.githubusercontent.com/46321485/229776848-68650062-b136-4caf-8d28-48418fb71c2a.png)

2) Start&End Activities Analysis

![Figure 2023-04-03 215434](https://user-images.githubusercontent.com/46321485/229776895-5fdd5c49-36f2-423a-bb7f-0544b91b435d.png)

3) Filtering
## 3. Process map 
1) Alpha_miner+petrinet

![Figure 2023-04-03 215028](https://user-images.githubusercontent.com/46321485/229776557-77bbdd8b-3a6a-4966-b247-0cc3ec7cd074.png)

2) Heuristic_net

![Heuristicminer](https://user-images.githubusercontent.com/46321485/229776468-93326d9a-a2ae-43c3-8198-ea07d8a078e6.png)

3) bpmn

![BPMN](https://user-images.githubusercontent.com/46321485/229776583-08b4916a-7167-4a20-8baa-93de561f5662.png)

4) Process_tree

![Processtree](https://user-images.githubusercontent.com/46321485/229776612-bcc3179a-f7bb-4ab4-ad16-85257d3b9b1d.png)

5) Directly followed graph(frequency, performance)
- Frequency(빈도)

![Figure 2023-04-03 214744](https://user-images.githubusercontent.com/46321485/229776646-b596f6ac-a02b-4341-853d-7057c29271d6.png)

- Performance(소요시간)

![Figure 2023-04-03 215023](https://user-images.githubusercontent.com/46321485/229776675-af22dcee-bdb8-4d9f-8727-7c86921ffd8a.png)




