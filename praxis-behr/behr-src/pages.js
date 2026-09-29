const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch();
 const p=await b.newPage({viewport:{width:1440,height:900}});
 await p.goto('file://'+process.cwd()+'/bundle.html'); await p.waitForTimeout(5000);
 for (const n of ['Start','Für dich','Ablauf und Kosten','Kontakt','Styleguide']){
   await p.getByRole('button',{name:n,exact:true}).first().click(); await p.waitForTimeout(800);
   const slug=n.replace(/\W+/g,'_');
   await p.screenshot({path:`p_${slug}.png`,fullPage:true});
   const html=await p.evaluate(()=>document.querySelector('[data-dc-tpl="13"]').outerHTML);
   fs.writeFileSync(`p_${slug}.html`,html);
   const txt=await p.evaluate(()=>document.querySelector('[data-dc-tpl="13"]').innerText);
   fs.writeFileSync(`p_${slug}.txt`,txt);
   console.log(n,html.length);
 }
 await b.close();
})();
