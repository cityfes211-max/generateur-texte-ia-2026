import streamlit as st
import random

st.set_page_config(page_title="مولد النص بالذكاء الاصطناعي", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center;'>🤖 مولد النص بالذكاء الاصطناعي 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>اكتب أي موضوع و الـ AI سيكتب لك فقرة كاملة</p>", unsafe_allow_html=True)

sujet = st.text_input("الموضوع ديالك:")

if st.button("✨ توليد النص"):
    if sujet:
        # هنا حطينا فقرة جاهزة. من بعد نقدر نربطوها بـ AI حقي
        reponses = [
            f"موضوع {sujet} من المواضيع المهمة جدا في وقتنا الحالي. حيث أن {sujet} يلعب دور كبير في حياتنا اليومية ويؤثر على طريقة تفكيرنا وعملنا. العديد من الخبراء يرون أن فهم {sujet} بشكل جيد يساعدنا على التطور وتحقيق أهدافنا. وفي المستقبل سيكون لـ {sujet} تأثير أكبر وأهمية متزايدة في جميع المجالات.",
            
            f"عندما نتحدث عن {sujet} يجب أن نعرف أنه ليس مجرد كلمة بل هو مفهوم واسع. {sujet} يتطلب منا البحث والتعلم المستمر. الكثير من الناس يهتمون بـ {sujet} لأنه يساعدهم على حل المشاكل وتطوير مهاراتهم. لذلك من الضروري أن نعطي {sujet} الأهمية التي يستحقها.",
            
            f"{sujet} هو واحد من أهم العناصر اللي خاصنا نركزو عليها. السبب هو أن {sujet} مرتبط مباشرة بالنجاح والتقدم. إذا فهمنا {sujet} مزيان غادي نقدرو نوصلو لنتائج أفضل. ولهذا كننصحو أي واحد بغا يتطور أنه يبدأ بتعلم {sujet}."
        ]
        
        texte_genere = random.choice(reponses)
        st.success("النص ديالك واجد:")
        st.write(texte_genere)
        
        st.download_button(
            label="📄 تحميل النص",
            data=texte_genere,
            file_name=f"texte_{sujet}.txt",
            mime="text/plain"
        )
    else:
        st.error("المرجو كتابة الموضوع أولا")
