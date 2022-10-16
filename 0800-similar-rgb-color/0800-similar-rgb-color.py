class Solution:
    def similarRGB(self, color):
        def geClosest(s):
            return min(['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'],
                key=lambda x: abs(int(s, 16) - int(x, 16)))

        res = [geClosest(color[i:i+2]) for i in range(1, len(color), 2)]
        return '#' + ''.join(res)
