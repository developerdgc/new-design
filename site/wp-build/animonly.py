import json
from restyle import *
allx=nodes(39); T=lambda t:by_title(allx,t); ops=[]
for t,a in [("About Media",("left",0)),("About Copy",("right",150)),("Audit Copy",("left",0)),("Audit Form Card",("right",150)),("Why Copy",("left",0)),("Why Media",("right",150))]:
    ops+=[{"action":"update","element_id":i,"interactions":anim(*a)} for i in T(t)]
ops+=[{"action":"update","element_id":i,"interactions":anim("bottom",0,"fade")} for i in T("Final CTA Banner")]
for k,t in enumerate(["SEO and Digital Marketing Card","GBP Optimization Card","Web Development Card","Social Media Marketing Card","Google Ads Card","Branding Card"]):
    ops+=[{"action":"update","element_id":i,"interactions":anim("bottom",(k%3)*120)} for i in T(t)]
print(len(ops),apply(39,ops))
