APIKEY=("sk-b0f54fe302014170851e0f7dda86af38")

from data import furnitureLIST
matching = {
    "预算2000左右": ["光年护脊", "活力护脊", "平安舒享"],
    "预算3000左右": ["白莲豪华", "欢乐颂活力"],
    "预算4000左右": ["蜜月黄金"],
    "预算5000左右": ["蜜月铂光"],
    "预算8500左右": ["净眠M80"],
    "预算25000左右": ["净眠BD624"],
    "想要最便宜的": ["光年护脊"],
    "预算不限就要最好的": ["净眠BD624"],
    "偏硬": ["活力护脊", "光年护脊", "平安舒享", "净眠BD624"],
    "偏软": ["蜜月黄金", "欢乐颂活力", "净眠M80"],
    "软硬适中": ["蜜月铂光"],
    "双面可调一床两睡": ["蜜月黄金", "蜜月铂光", "活力护脊", "白莲豪华"],
    "护脊": ["活力护脊", "光年护脊"],
    "老人腰背需要支撑": ["活力护脊", "光年护脊", "平安舒享"],
    "小孩青少年护脊": ["活力护脊", "光年护脊", "平安舒享"],
    "孕妇侧睡抗干扰": ["蜜月铂光"],
    "体重大强支撑": ["活力护脊"],
    "体型偏瘦柔软贴合": ["欢乐颂活力", "净眠M80"],
    "侧睡": ["蜜月黄金", "蜜月铂光", "净眠M80"],
    "仰睡": ["平安舒享", "活力护脊", "光年护脊"],
    "俯睡趴睡": ["光年护脊", "净眠BD624"],
    "怕热爱出汗": ["蜜月铂光", "欢乐颂活力", "净眠M80"],
    "冬天怕冷要保暖": ["净眠BD624"],
    "自动调温": ["净眠M80", "净眠BD624"],
    "抗干扰不怕伴侣翻身": ["蜜月黄金", "蜜月铂光", "平安舒享", "光年护脊", "白莲豪华", "净眠M80"],
    "两人睡感不同要折中": ["蜜月黄金", "蜜月铂光", "白莲豪华"],
    "担心甲醛": ["净眠M80", "光年护脊"],
    "婴儿皮肤敏感": ["蜜月黄金", "净眠M80"],
    "鼻炎粉尘过敏": ["蜜月黄金", "活力护脊", "平安舒享", "白莲豪华"],
    "怕胶水味": ["光年护脊"],
    "环保天然材质": ["光年护脊", "白莲豪华"],
    "新婚夫妻": ["蜜月黄金"],
    "年轻人追求颜值": ["欢乐颂活力"],
    "送父母长辈": ["活力护脊", "光年护脊", "平安舒享"],
    "租房过渡": ["光年护脊"],
    "主卧舒适": ["蜜月铂光", "净眠M80", "净眠BD624"],
    "次卧性价比": ["光年护脊", "活力护脊", "平安舒享"],
    "高箱床要厚": ["净眠M80"],
    "榻榻米要薄": ["活力护脊"],
    "第一次买不知道选什么": ["蜜月黄金", "白莲豪华"],
    "之前睡太硬想换软": ["欢乐颂活力", "净眠M80"],
    "之前睡太软想换硬": ["活力护脊", "光年护脊", "净眠BD624"],
    "一步到位十年不换": ["净眠M80", "净眠BD624"],
    "追求面子旗舰款": ["净眠BD624"],
    "追求科技感黑科技": ["净眠M80"],
    "想要最贵的": ["净眠BD624"]
}
def recommendation(x):
    rlist=[]
    finallist=[]
    for i in matching:
        if i in x:
            rlist.extend(matching[i])
    for m in rlist:
        if m not in finallist:
            finallist.append(m)
        
    return finallist

if __name__=="__main__":
    
    while True:
        n=input("请输入你的需求(输入exit退出): ")
        result=recommendation(n)
        if result:
            print(result)
        elif n=="exit":
            break
        else:
            print("没有匹配床垫，请换个关键词")
            

def matches(x):
    mlist=[]
    for i in furnitureLIST:
        if x in i["名字"]:
            mlist.append(i)
    return mlist




def new(n):
    nlist=[]
    for i in n:
        nlist.extend(matches(i))
    return nlist



def chat(n):
    clist=[]
    clist.extend(new(recommendation(n)))
    if clist==[]:
        return "抱歉，根据您的描述，我暂时没找到完全匹配的床垫，您方便的话可以来店里看看，我们有更多款式可以体验。(好百年家具广场：江西省宜春市樟树市四特大道2号樟树国际家居建材城1号楼)"
    else:
        return clist
    
def reply(n):
    information=[]
    n=chat(n)
    if isinstance(n,list):
        for idx,item in enumerate(n,1):
            sec=str(idx)+"."+ item['名字']+'\n'+ str(item['价格'])+"元"+'\n'+ item['尺寸']+'\n'+ item['卖点']
            information.append(sec)
        return "\n".join(information)
    elif type(n)==str:
        return n
print(reply("预算2000左右"))