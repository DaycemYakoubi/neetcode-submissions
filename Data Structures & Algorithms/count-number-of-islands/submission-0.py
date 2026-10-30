from collections import deque,defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #transform the grid to a graph
        R,C=len(grid),len(grid[0])
        nodes=[]
        graph=defaultdict(list)
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='0':
                    continue
                nodes.append((r,c))
                for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]!='0':
                        graph[(r,c)].append((nr,nc))
        #count the connex composants
        seen=set()
        count=0
        for s in nodes:
            if s in seen:
                continue
            count+=1
            seen.add(s)
            q=deque([s])
            while q:
                u=q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
        return count
