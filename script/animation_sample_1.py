import bpy
import time
import csv

class ShopConnectSample(bpy.types.Panel):
    bl_label = "ShopInfo"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AddPanel"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="ショップ情報", icon='WORLD_DATA')

        row = layout.row()
        row.operator("mycustom.button")

        row = layout.row()
        row.label(text="売り子一覧", icon='WORLD_DATA')

        row = layout.row()
        row.operator("mycustom.button")

        row = layout.row()
        row.label(text="商品一覧", icon='WORLD_DATA')



class ShopCusttomButton(bpy.types.Operator):
    bl_idname = "mycustom.button"
    bl_label = "execute"

    @classmethod
    def poll(cls, context):
        print("myint print")

        return{"FINISHED"}

class MyIntPropertyGroup(bpy.types.PropertyGroup):
    myint : bpy.props.IntProperty(
        name="myint_name",     # 変数名
        description="",        # 説明文
        default=1,             # デフォルト値
        min=1,                 # 最小値
        max=10,                # 最大値
    )

regist_classes = (
    ShopConnectSample,
    ShopCusttomButton,
    MyIntPropertyGroup
)

for regist_cls in regist_classes:
    bpy.utils.register_class(regist_cls)

locations = []

# アニメーションマスターを編集する.
# アクションと紐づけたりする企画側が入力する
with open("D:\\devellop\\DigitalPortal\\ContentsArtChallenge\\technicalartchallenge\\script\\animation.csv", newline='') as animationcsv:

    boxreader = csv.reader(animationcsv, delimiter=",")
    # x,y, zの順番でデータを設定
    for row in boxreader:
        locations.append([int(row[0]), int(row[1]), int(row[2])])



# blenderでアニメーションをさせるオブジェクトを一つ指定する
obj = bpy.context.scene.objects[0]


i = 0
for location in locations:
    print(location)
    obj.location = location
    obj.keyframe_insert(data_path="location", frame=10.0*i)
    i += 1
