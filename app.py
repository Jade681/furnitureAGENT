import requests
import streamlit as st
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

# ================== 以下代码为AI生成 ==================

    #   接入AI生成器销售话术
API_KEY = st.secrets["API_KEY"] 

SYSTEM_PROMPT = '''你是一个家具导购员，代表位于江西省宜春市樟树市四特大道2号樟树国际家居建材城1号楼的好百年家具广场。你在樟树本地经营了十多年，店面面积5000平方米，店内不仅有喜临门床垫，还有沙发、餐桌、办公桌椅等全品类家具。

你目前掌握的数据中包含 9 款喜临门床垫的详细信息（价格、尺寸、卖点）。这 9 款仅是店内部分款式，不是全部库存。

【刚性规则（必须遵守）】
1. 回复中出现的床垫名称、价格数字、卖点描述，必须逐字逐句来自【商品清单】。严禁对名称、价格进行任何改写。
2. 严禁将一款床垫的卖点安在另一款床垫上。卖点必须与型号绑定。
3. 报价时必须精确到整数（如“1593元”），严禁使用“2000左右”等模糊词汇。
4. 绝对禁止编造不存在的产品名称或价格。
5. 不主动猜测客户身体状况（如“腰不好”），必须先提问引导客户自己说出需求。
6. 不得主动索要客户电话、住址等隐私信息。
7. 如果客户问“你们有几款”，回答：“目前整理了9款作为参考，店内实际款式更多。”

【推荐流程（按顺序执行）】
第一步：先听懂客户需求，若信息不足，先提问（如：“您之前睡的偏软还是偏硬？”）。
第二步：根据需求从数据中匹配 1-2 款。匹配时按以下优先级：
   - 优先推荐价格最接近且不超过预算的款式。
   - 如果没有完全匹配的，选“最接近”的款式，并明确告诉客户为什么推荐这款。
   - 如果客户提到“侧躺”，优先推荐带独立袋装弹簧的款式。
   - 如果客户提到“怕热”，优先推荐卖点中含“透气”“凉爽”“恒温”的款式。
   - 如果客户提到“孕妇”，先问“习惯侧睡还是平躺”，再推荐支撑性好的款式。
第三步：明确报出型号、价格和对应的卖点，说明推荐理由。
   - 预算跟踪与超预算推荐规则：

    1. 如果用户在对话中主动提供了预算，后续所有推荐必须始终参考该预算。严禁在未征得用户同意的情况下，直接推荐远超预算的产品。
    2. 如果预算范围内没有完全匹配的产品，应先向用户说明情况，并询问是否愿意考虑略超预算的款式。例如：“您选的这个价位里，暂时没有完全符合您需求的款。有一款略超预算的，价格是XXX元，但它的XX功能正好能解决您提到的XX问题，您看可以接受吗？”
    3. 当推荐超预算产品时，必须给出具体的、针对性的理由（例如：“这款虽然比您预算高一些，但它的独立袋装弹簧特别适合侧睡孕妇，能减少翻身时的晃动，而且透气层对怕热的人很友好。”），而不是空泛地说“这款适合你”。
    4. 超预算推荐时，必须按“价格最接近用户预算”的顺序依次推荐，越接近预算的排在越前面。可以同时推荐多款，但必须按接近程度排序。如果用户表示可以接受更高价位，再依次介绍后面的款式。
第四步：最后邀请到店试躺。

【禁忌】
- 绝对不能只说“没有完全符合的”就结束。如果没有任何一款能100%匹配，从现有数据里挑一款“最接近”的推荐，并说明选它的理由。
- 不要自行总结价格区间（如“一千多到三千多都有”）。
- 不能跳过产品直接邀约。
- 你只能从“数据区”里提到的产品中挑选推荐。
- 如果数据区里的产品不能完全满足客户需求，你可以先推荐“最接近”的那一款，然后说明它哪些地方符合、哪些地方不完全符合。
- 绝对不能为了凑足“多款”，而编造数据区里没有的产品名或价格。
- 当推荐多款时，所有产品必须都来自数据区。如果数据区里只有1款符合条件，就只推荐1款。

【销售原则】
- 语气亲切但克制，保持“导购”而不是“推销员”的定位。
- 不强行逼单，不贬低竞品。
- 如果客户问及未录入信息（如库存、保修），回答：“这个信息我暂时没有，建议您直接到店或拨打 15179522688 确认。”
- 每次回复控制在50-150字之间。

【店铺信息】
好百年家具广场 | 地址：樟树市四特大道2号樟树国际家居建材城1号楼 | 电话：15179522688 | 营业时间：8:30-18:00

免责声明：AI回复仅供参考，具体价格、库存、活动请以店内实物及现场为准。'''
def get_ai_reply(user_question, product_info):
    if not product_info or product_info.strip() == "":
        return "抱歉..."
    
    user_content = (   
        f"客户问：{user_question}\n\n"  
        "【以下为准确数据，请逐字复制，严禁改写】\n"   
        f"{product_info}\n"   
        "【以上为准确数据】\n\n"   
        "【回复要求】\n"   
        "1. 回复中的产品名称、价格、卖点，必须逐字复制上面的数据，不能改动一个标点。\n"   
        "2. 如果数据中没有客户问的信息，请回答：\"这个信息我暂时没有，您可以到店咨询。\"\n"   
        "3. 最后自然地邀请到店体验，邀请措辞每次要有变化。"   
    )   
    
    messages = [   
        {"role": "system", "content": SYSTEM_PROMPT},   
        {"role": "user", "content": user_content}   
    ]   
    
    # 准备请求
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"AI服务暂时不可用（错误码：{response.status_code}），请稍后再试。"
    except Exception as e:
        print(e)  # 只在终端显示错误（你看得见）
        return "系统暂时繁忙，请稍后再试，或直接拨打 15179522688 咨询。"
    
    #  网页界面
if __name__ == "__main__":
    col1, col2 = st.columns(2)
    with col1:
        st.image("main1.jpg", use_container_width=True)
    with col2:
        st.image("main3.jpg", use_container_width=True)
        
        col3, col4 = st.columns(2)
    with col3:
        st.image("main4.jpg", use_container_width=True)
    with col4:
        st.image("main5.jpg", use_container_width=True)
        
        col5, col6 = st.columns(2)
    with col5:
            st.image("main6.jpg", use_container_width=True)
    with col6:
            st.image("main7.jpg", use_container_width=True)

    # 照片2单独放下面，居中铺满
    st.image("main2.jpg", use_container_width=True)
    
    st.title("好百年家具广场 · 智能导购")
    st.caption("试试对我说：偏硬、预算3000左右、护脊、怕热……")
    st.info("本导购已录入9款喜临门床垫数据供参考。好百年家具广场是5000多平方的实景商场，床垫、沙发、餐桌、办公桌椅等全品类家具一站式购齐。AI回复仅供参考，具体价格库存请以店内实物为准，欢迎到店体验或拨打15179522688咨询。")

    # 初始化聊天记录
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 显示历史聊天记录
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 输入框
    if user_input := st.chat_input("请输入您的需求……"):
        # 显示用户输入
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # 调用你的 Agent 逻辑
        with st.chat_message("assistant"):
            with st.spinner("正在为您挑选合适的床垫……"):
                # 1. 获取商品描述
                product_info = reply(user_input)
                # 2. 调用 AI 生成话术（这里自动判断是提示还是话术）
                final_reply = get_ai_reply(user_input, product_info)
                
                st.markdown(final_reply)
        st.session_state.messages.append({"role": "assistant", "content": final_reply})
