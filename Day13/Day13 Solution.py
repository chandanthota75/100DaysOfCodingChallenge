class Solution:
    def isSumString(ob, S):
        def check_sum(string, start, len1, len2):
            substring1 = string[start: start + len1]
            substring2 = string[start + len1: start + len1 + len2]
            sum_result = string_sum(substring1, substring2)
        
            sum_result_len = len(sum_result)
            if sum_result == string[start + len1 + len2: start + len1 + len2 + sum_result_len]:
                if start + len1 + len2 + sum_result_len == len(string):
                    return True
                return check_sum(string, start + len1, len2, sum_result_len)
            return False


        def string_sum(str1, str2):
            if len(str1) < len(str2):
                str1, str2 = str2, str1
        
            m = len(str1)
            n = len(str2)
            ans = ""
            carry = 0
            
            for i in range(n):
                ds = (ord(str1[m - 1 - i]) - ord('0') + ord(str2[n - 1 - i]) - ord('0') + carry) % 10
                carry = (ord(str1[m - 1 - i]) - ord('0') + ord(str2[n - 1 - i]) - ord('0') + carry) // 10
                ans = str(ds) + ans
                
            for i in range(n, m):
                ds = (ord(str1[m - 1 - i]) - ord('0') + carry) % 10
                carry = (ord(str1[m - 1 - i]) - ord('0') + carry) // 10
                ans = str(ds) + ans
            if carry:
                ans = str(carry) + ans
            return ans


        n = len(S)
        for i in range(1, n):
            for j in range(1, n - i):
                if check_sum(S, 0, i, j):
                    return 1
        return 0