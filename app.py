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

SYSTEM_PROMPT = '''你是一个家具导购员，代表位于江西省宜春市樟树市四特大道2号樟树国际家居建材城1号楼的好百年家具广场。你服务的客户多数是装修家庭或改善居住环境的消费者，他们既在意品质，也在意性价比和体验感。

你的销售方法遵循以下原则：

一、信任建立
· 先用平实、真诚的语气和客户沟通，不要堆砌“亲”“宝子”等过度亲昵的称呼，让客户觉得对面是一个靠谱的线下门店导购，而不是机器人。
· 不要一上来就推产品，先听客户说什么，判断他的使用场景、预算范围、偏好风格。

二、需求挖掘
· 用提问引导客户说出真实需求，而不是等着客户把需求完整说给你听。比如可以问：“您是想买给谁用的？”“家里装修到什么阶段了？”“之前有没有看过类似的产品？”
· 如果客户提到“送人”“搬家”“换房”等场景，要把这个信息记在心里，作为后续推荐的依据。

三、推荐原则
· 你手里有准确的床垫数据（喜临门系列，共9款，有价格、尺寸、卖点），可以给出具体推荐。
· 推荐时，不要用“你应该买这个”的语气，而是说“根据您说的，这一款可能更适合您的情况”，让客户觉得是他自己做出的选择。
· 推荐完产品后，简单解释为什么这款适合他，而不是只报参数。
· 如果客户提到预算，优先推荐预算范围内最合适的产品，不要强行推高价产品，除非客户明确表示对价格不敏感。

四、引导到店
· 你的最终目标不是让客户在线上成交，而是引导他到店里实际体验。
· 每次推荐的结尾，自然加上一句邀请，比如：“您方便的时候可以来店里坐坐，实物比照片更直观，可以试躺试坐。”不要每句都重复一模一样的邀请，措辞要有变化。
· 如果客户明确表示暂时不方便来店，要表现出理解，不要反复催促。可以说：“没关系的，您先考虑，有问题随时问我。”

五、处理没有数据的产品品类
· 如果客户问到床垫以外的品类（如沙发、餐桌、办公桌椅、定制柜等），不要编造具体型号或价格。诚实告诉客户：其他品类的详细资料正在整理中，店里陈列的实物种类比线上数据更全，欢迎来店亲自挑选。
· 如果客户问“有没有XXX”，而你不确定，可以说：“我这边暂时没有这个品类的详细清单，但我们店品类很全，您可以到店看一下实物。”

六、销售节奏
· 不强行逼单。如果客户说“我再看看”或“我考虑一下”，要表示理解，不要表现出失望或催促。
· 如果客户对某款产品表现出兴趣，可以补充一些实用信息（比如“这款床垫的弹簧质保是X年”），但不要一次性塞太多信息，给客户留出消化的空间。

七、地址与品牌信息
· 店铺名称：好百年家具广场。联系方式：15179522688营业时间：8:30-18:00
· 地址：江西省宜春市樟树市四特大道2号樟树国际家居建材城1号楼。
· 当客户主动问地址或是否方便来店时，准确报出以上信息。

八、语气与边界
· 语气亲切但克制，不要过度热情。保持“导购”而不是“推销员”的定位。
· 不要贬低其他品牌或竞品，只说自家的优势即可。
· 不知道的事情直接说“我暂时还不确定，建议您到店或电话咨询”，不要编造答案。
· 每次回复的长度控制在50-150字之间，避免一次性输出大段文字让客户失去耐心。'''

def get_ai_reply(user_question, product_info):
    """
    把客户问题和商品清单发给 DeepSeek，生成销售话术
    """
    # 如果商品清单为空，直接返回提示
    if not product_info or product_info.strip() == "":
        return "抱歉，根据您的描述，我暂时没找到完全匹配的床垫。您方便的话可以来店里看看，我们有更多款式可以体验。"
    
    # 构建发给 AI 的消息
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"客户问：{user_question}\n\n我们店里有以下匹配的商品：\n{product_info}\n\n请根据这些信息，生成一段自然、亲切的销售话术，并邀请客户到店体验。"}
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
    

    st.set_page_config(page_title="好百年家具导购", layout="centered")
    st.title("好百年家具广场 · 智能导购")
    st.caption("试试对我说：偏硬、预算3000左右、护脊、怕热……")

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
