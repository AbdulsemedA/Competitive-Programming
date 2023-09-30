m, s = map(int, input().split())
if m==1 and s==0:
    print(0, 0)
elif m==1 and s==1:
    print(1, 1)
else:
    if m >= s:
        if s == 0:
            print(-1,-1)
        else:
            if s > 9:
                curr = s
                ans = ''
                total = 0
                back = ''

                while curr >= 9:
                    curr -= 9
                    ans = '9' + ans
                    total += 1
                
                if curr > 0:
                    if m - total == 2:
                        back = ans + str(curr) + '0'
                        ans = '1' + str(curr-1) + ans
                    elif m - total > 2:
                        back = ans + str(curr) + '0' * (m - total - 1)
                        ans = '1' + '0' * (m- total- 2) + str(curr-1) + ans
                    else:
                        ans = str(curr) + ans
                        back = ans[::-1]
                else:
                    back = ans + '0' * (m - len(ans))
                
                if len(ans) < m:
                    if m - len(ans):
                        ans = '1' + '0' * (m - len(ans) - 1) + str(int(ans[0]) - 1) + ans[1:]
                        
                if len(ans) == m:
                    print(ans, back)
                else:
                    print(-1,-1)
            else:
                print('1' + '0' * (m - 2) + str(s - 1)
                      , str(s) + '0' * (m - 1))
    else:
        if s > 9:
            curr = s
            ans = ''
            total = 0
            back = ''

            while curr >= 9:
                curr -= 9
                ans = '9' + ans
                total += 1
            
            if curr > 0:
                if m - total == 2:
                    back = ans + str(curr) + '0'
                    ans = '1' + str(curr-1) + ans
                elif m - total > 2:
                    back = ans + str(curr) + '0' * (m - total - 1)
                    ans = '1' + '0' * (m- total- 2) + str(curr-1) + ans
                else:
                    ans = str(curr) + ans
                    back = ans[::-1]
            else:
                back = ans + '0' * (m - total)
            
            if len(ans) < m:
                if m - len(ans):
                    ans = '1' + '0' * (m - len(ans) - 1) + str(int(ans[0]) - 1) + ans[1:]
                    
            if len(ans) == m:
                print(ans, back)
            else:
                print(-1,-1)
        else:
            curr = 0
            ans = ''
            sm = s
            while curr < m - 1:
                if not curr:
                    ans += '1'
                    sm -= 1
                else:
                    ans += '0'
                
                curr += 1
            ans += str(sm)

            print(ans, str(s) + '0' * (m-1))