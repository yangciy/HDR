import json,os
import pandas as pd

# path=('/Users/uk/Desktop/[라벨]바벨_덤벨_Labeling//Users/uk/Desktop')
# path=[s for s in path if "DS_Store" not in s]
# # print(path)
point=['Nose','Left Eye','Right Eye','Left Ear','Right Ear','Left Shoulder','Right Shoulder','Left Elbow','Right Elbow','Left Wrist','Right Wrist',
            'Left Hip','Right Hip','Left Knee','Right Knee','Left Ankle','Right Ankle','Neck','Left Palm','Right Palm','Back','Waist','Left Foot','Right Foot',
            ]
point_name=['Nose','LeftEye','RightEye','LeftEar','RightEar','LeftShoulder','RightShoulder','LeftElbow','RightElbow','LeftWrist','RightWrist',
'LeftHip','RightHip','LeftKnee','RightKnee','LeftAnkle','RightAnkle','Neck','LeftPalm','RightPalm','Back','Waist','LeftFoot','RightFoot',
]
views=['view1','view2','view3','view4','view5']
aa=[]


files=os.listdir('/Users/uk/Downloads/013/라벨링데이터')
# print(files)
# for folder in path:
#     files=os.listdir(f'/Users/uk/Desktop/[라벨]바벨_덤벨_Labeling/{folder}')

    # print(files)
# files_2d=[s for s in files if ".DS_Store" not in s]
files_2d=[s for s in files if "3d" not in s]
print(files_2d)
# if files_2d is None:
#     continue
for load in files_2d:

    # print(load)
    with open(f'/Users/uk/Downloads/013/라벨링데이터/{load}', "r", encoding='unicode-escape') as f:
        contents = f.read() # string 타입
        json_data = json.loads(contents)
        num=len(json_data['frames'])

        for i in range(num):
            for j in views:
                for n,k in enumerate(point):
                    globals()[f'{point_name[n]}_x']=json_data['frames'][i][j]['pts'][k]['x']
                    globals()[f'{point_name[n]}_y']=json_data['frames'][i][j]['pts'][k]['y']
                    jpg_name=json_data['frames'][i][j]['img_key']
                b=[jpg_name,Nose_x,Nose_y,LeftEye_x,LeftEye_y,RightEye_x,RightEye_y,LeftEar_x,LeftEar_y,RightEar_x,RightEar_y,
                    LeftShoulder_x,LeftShoulder_y,RightShoulder_x,RightShoulder_y,LeftElbow_x,LeftElbow_y,RightElbow_x,RightElbow_y,
                    LeftWrist_x,LeftWrist_y,RightWrist_x,RightWrist_y,LeftHip_x,LeftHip_y,RightHip_x,RightHip_y,LeftKnee_x,LeftKnee_y,
                    RightKnee_x,RightKnee_y,LeftAnkle_x,LeftAnkle_y,RightAnkle_x,RightAnkle_y,Neck_x,Neck_y,LeftPalm_x,LeftPalm_y,
                    RightPalm_x,RightPalm_y,Back_x,Back_y,Waist_x,Waist_y,LeftFoot_x,LeftFoot_y,RightFoot_x,RightFoot_y]
                # print(len(b))
                aa.append(b)
                # print(a)

                #   print(a)
                #   print(b)
            
aaa=pd.DataFrame(aa,columns=['jpg_name','Nose_x','Nose_y','LeftEye_x','LeftEye_y','RightEye_x','RightEye_y','LeftEar_x','LeftEar_y','RightEar_x','RightEar_y',
            'LeftShoulder_x','LeftShoulder_y','RightShoulder_x','RightShoulder_y','LeftElbow_x','LeftElbow_y','RightElbow_x','RightElbow_y',
            'LeftWrist_x','LeftWrist_y','RightWrist_x','RightWrist_y','LeftHip_x','LeftHip_y','RightHip_x','RightHip_y','LeftKnee_x','LeftKnee_y',
            'RightKnee_x','RightKnee_y','LeftAnkle_x','LeftAnkle_y','RightAnkle_x','RightAnkle_y','Neck_x','Neck_y','LeftPalm_x','LeftPalm_y',
            'RightPalm_x','RightPalm_y','Back_x','Back_y','Waist_x','Waist_y','LeftFoot_x','LeftFoot_y','RightFoot_x','RightFoot_y'])
print(aaa.info())
aaa.to_csv('dfdsaf.csv',index=False)