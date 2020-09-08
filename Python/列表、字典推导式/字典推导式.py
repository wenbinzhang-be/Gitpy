# 字典推导式作用： 快速合并列表或提取字典中目标数据
# dict1 = {i: i**2 for i in range(5)}
# print(dict1)
data = ' BAIDUID=1932283F00F9DC8DD79298A90D33B5B9:FG=1; BIDUPSID=1932283F00F9DC8DD79298A90D33B5B9; PSTM=1595919346; BD_UPN=12314753; BDUSS=5RQzM0d3lOVnQyWH43a0xsRzdDUm5hblZ6QWxDR0lHNHFyNVdCVlZJdkpCbVpmRVFBQUFBJCQAAAAAAAAAAAEAAADhGTqCuMmy8cHSu~C1xMfvzOwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMl5Pl~JeT5fS3; BDUSS_BFESS=5RQzM0d3lOVnQyWH43a0xsRzdDUm5hblZ6QWxDR0lHNHFyNVdCVlZJdkpCbVpmRVFBQUFBJCQAAAAAAAAAAAEAAADhGTqCuMmy8cHSu~C1xMfvzOwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMl5Pl~JeT5fS3; COOKIE_SESSION=565850_6_1_0_9_5_1_1_0_1_3_1_0_0_2_4_1598527343_1596940308_1599093191%7C4%230_2_1596940304%7C1; __yjsv5_shitong=1.0_7_4e775e69712eb508d1b0de25288abab7e049_300_1599142661794_111.21.177.26_c64b2e4a; yjs_js_security_passport=fba78dd1dd5b3e0bb90ab277607798144ad9245c_1599142662_js; BDRCVFR[bIKc3BPCk_C]=OjjlczwSj8nXy4Grjf8mvqV; BD_HOME=1; H_PS_PSSID=32606; BDRCVFR[HaZoM-yKXvb]=OjjlczwSj8nXy4Grjf8mvqV; sug=3; sugstore=1; ORIGIN=0; bdime=0'
# 列表推导
# cookies_list = data.split(';')
# cookies = {cookie.split('=')[0]: cookie.split('=')[-1]for cookie in cookies_list}
# print(cookies)
# for 循环
cookies_list = data.split(';')
cookies = {}
for cookie in cookies_list:
    cookies[cookie.split('=')[0]] = cookie.split('=')[-1]

print(cookies)


