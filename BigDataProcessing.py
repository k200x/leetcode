#coding:utf-8


# 然后尝试了一下，发现速度并没有多少提示，看了一下资源使用率，只占满了1个核，不能满足要求
# from multiprocessing.dummy import Pool as ThreadPool
#
# pool = ThreadPool(20)
# # pool.map(func_name, args)
# pool.close()
# pool.join()


# 但是尝试了一下，还是只跑了一个核，依然失败
# from dask import delayed
# import dask.bag as db
# L = []
# for fn in encrypt_files:
#     b = db.read_text(fn)
#     a = delayed(decrypt_file)(fn)          # Delay execution of function
#     L.append(a)
# result = delayed(L)
# result.compute()


# 测试了一下，可以跑满多个核心，其使用的CPU核心数量就是设定的那个数量。
# 但是也存在一个问题，就是程序跑一段时间后就会效率下降，监控一下CPU发现也只剩下一个核心在跑了，目前还不知道是什么原因，也没有深究
# cpu_num = 1
# job_server = pp.Server(cpu_num)
# a =  []
# for f in fn:
#     a.append(job_server.submit(fun_name, (f, ), (fun_1, fun_2, ), ('sys', 'datetime', 'pp', )))
# for x in a:
# tmp = x()
























