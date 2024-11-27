from collections import defaultdict
to_index = lambda word: (ord(word[0]) - ord('a'), ord(word[-1]) - ord('a'))

def make_graph(words):
    adj = [[0] * 26 for _ in range(26)] # 알파벳 문자의 인접 행렬(간선의 수)
    graph = defaultdict(list) # graph[(i,j)]: i로 시작해서 j로 끝나는 단어 목록
    indeg = [0] * 26 # indeg[i]: i로 시작하는 단어의 수
    outdeg = [0] * 26 # outdeg[i]: i로 끝나는 단어의 수
    for i in range(len(words)):
        a, b = to_index(words[i])
        graph[(a, b)].append(words[i])
        adj[a][b] += 1
        outdeg[a] += 1
        indeg[b] += 1
    return adj, graph, indeg, outdeg

def checkEuler(indeg, outdeg):
    plus1, minus1 = 0, 0
    for i in range(26):
        delta = outdeg[i] - indeg[i]
        if delta < -1 or delta > 1:
            return False  # 정점 차수가 -1, 0, 1 이외면 경로 없음
        if delta == 1:
            plus1 += 1
        if delta == -1:
            minus1 += 1
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)

def getEulerCircuit(here, circuit, adj):
    for there in range(len(adj)):
        while adj[here][there] > 0:  # 현재 정점에서 갈 수 있는 모든 간선 탐색
            adj[here][there] -= 1  # 사용한 간선을 제거 (multigraph 고려)
            getEulerCircuit(there, circuit, adj)  # 다음 정점으로 이동
    circuit.append(here)  # 모든 간선을 사용한 후 정점을 경로에 추가

def getEulerTrailOrCircuit(adj, indeg, outdeg):
    circuit = []
    for i in range(26):
        if outdeg[i] == indeg[i] + 1:  # 시작점 후보
            getEulerCircuit(i, circuit, adj)
            return circuit
    for i in range(26):
        if outdeg[i] != 0:  # 간선이 있는 정점에서 회로 찾기
            getEulerCircuit(i, circuit, adj)
            return circuit
    return circuit  # 실패 시 빈 리스트 반환

def wordchain(words):
    adj, graph, indeg, outdeg = make_graph(words)
    if not checkEuler(indeg, outdeg):  # 오일러 조건 불만족 시 "IMPOSSIBLE"
        return "IMPOSSIBLE"
    circuit = getEulerTrailOrCircuit(adj, indeg, outdeg)
    if len(circuit) != len(words) + 1:  # 모든 간선을 방문하지 못한 경우
        return "IMPOSSIBLE"
    circuit.reverse()  # 오일러 경로 순서를 역순으로
    ret = ""
    for i in range(1, len(circuit)):
        a, b = circuit[i - 1], circuit[i]
        if len(ret) != 0:
            ret += " "
        ret += graph[(a, b)][-1]
        graph[(a, b)].pop()
    return ret

for _ in range(int(input())):
    n = int(input())  # 단어의 수
    words = [input() for _ in range(n)]  # 게임에 사용될 단어 목록
    print(wordchain(words))  # 결과 출력
