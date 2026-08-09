class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}                              # 篮子登记表：种类 type -> 个数 quantity
        left = 0                                # 窗口左端 window left boundary
        best = 0                                # 历史最长 running maximum

        for right in range(len(fruits)):
            # ── 进货 EXPAND：把 fruits[right] 加入窗口 ──
            f = fruits[right]
            count[f] = count.get(f, 0) + 1      # .get(f,0) 防 KeyError

            # ── 出货 SHRINK：种类超过 2 就从左边挤出去 ──
            while len(count) > 2:               # len(dict) 是 O(1)
                g = fruits[left]
                count[g] -= 1
                if count[g] == 0:
                    del count[g]                # ⭐ 归零必须删！否则 len 虚高
                left += 1

            # ── 结算 UPDATE：此刻窗口一定合法 ──
            best = max(best, right - left + 1)  # ⭐ 别忘 +1

        return best