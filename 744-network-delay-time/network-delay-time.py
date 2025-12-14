class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float("inf")
        nodes_dst = [inf] * n
        nodes_dst[k-1] = 0

        for _ in range(n):
            updated = False
            for u, v, c in times:
                if nodes_dst[u-1] != inf and nodes_dst[u-1] + c < nodes_dst[v-1]:
                    nodes_dst[v-1] = nodes_dst[u-1] + c
                    updated = True

            if not updated:
                break
        
        max_dst = -1
        for nodes in nodes_dst:
            if nodes == inf:
                return -1
            if nodes > max_dst:
                max_dst = nodes
        
        return max_dst