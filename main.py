import Identify
import OriMarkerIden

flag = True
type2s_enzymes = ["BsmBI","BsaI","BbsI","AarI","SapI"]
print('welcome to auto identification tool\n')
while(flag):
    seq = str(input("输入序列\n"))
    if(seq != ""):
        scar_result = Identify.scarFunction(seq)
        ori_marker_result = OriMarkerIden.FittingLabels(seq)
        print("Scar Information:\n")
        print(f'{type2s_enzymes[0]}:{scar_result[0]}\n'+
              f'{type2s_enzymes[1]}:{scar_result[1]}\n'+
              f'{type2s_enzymes[2]}:{scar_result[2]}\n'+
              f'{type2s_enzymes[3]}:{scar_result[3]}\n'+
              f'{type2s_enzymes[4]}:{scar_result[4]}\n')
        print("Ori and Marker Information: \n")
        print(f'Origin: {ori_marker_result['Origin']}')
        print(f'Marker: {ori_marker_result['Marker']}')
    choice = str(input("要退出吗？[y|n]"))
    if(choice == 'y'):
        flag = False
