#import main.py #NE MARCHE PAS POUR LE MOMENT
def allPathR(lst):
    if len(lst)==1:
        return [lst]
    
    lstRes=[]
    for a in lst:
        remainLst=[x for x in lst if x!=a]
        lstRecur=allPathR(remainLst)
        print(lstRecur)

matrix=[
[30.610455730027933, 19.235384061671343, 7.211102550927978, 17.08800749063506, 10.816653826391969, 18.110770276274835, 18.973665961010276, 6.4031242374328485],
[19.235384061671343, 21.0, 15.297058540778355, 9.486832980505138, 13.45362404707371, 5.0990195135927845, 9.055385138137417, 17.0],
[7.211102550927978, 15.297058540778355, 23.430749027719962, 16.97056274847714, 13.0, 16.1245154965971, 18.439088914585774, 11.0],
[17.08800749063506, 9.486832980505138, 16.97056274847714, 30.14962686336267, 7.0, 4.47213595499958, 2.0, 12.041594578792296],
[10.816653826391969, 13.45362404707371, 13.0, 7.0, 31.622776601683793, 9.848857801796104, 9.0, 5.0990195135927845],
[18.110770276274835, 5.0990195135927845, 16.1245154965971, 4.47213595499958, 9.848857801796104, 26.019223662515376, 4.0, 14.317821063276353],
[18.973665961010276, 9.055385138137417, 18.439088914585774, 2.0, 9.0, 4.0, 30.01666203960727, 14.035668847618199],
[6.4031242374328485, 17.0, 11.0, 12.041594578792296, 5.0990195135927845, 14.317821063276353, 14.035668847618199, 32.64965543462902],
]

matrix_3_3 = [
    [30,19,7],
    [19,21,9],
    [7,15,23]
]