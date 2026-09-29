import importlib,sys,json,re
mod=importlib.import_module(sys.argv[1]); parent=json.loads(sys.argv[2]); pos=sys.argv[3]; done=set(json.loads(sys.argv[4]) if len(sys.argv)>4 else [])
acts=[]
for label,h in mod.S:
    cls=set(re.findall(r'class="([^"]+)"',h))
    new=cls-done; done|=cls
    css=mod.c.only(new)
    a={"build_label":label,"parent_element_id":parent,"creation_position":pos,"html":h}
    if css: a["css"]=css
    acts.append(a)
json.dump(acts,open(sys.argv[1]+'_actions.json','w'),ensure_ascii=False)
json.dump(sorted(done),open(sys.argv[1]+'_classes.json','w'))
print([ (a['build_label'],len(a['html']),len(a.get('css',''))) for a in acts])
