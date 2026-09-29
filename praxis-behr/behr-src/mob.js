const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:390,height:844}});
 await p.goto('file://'+process.cwd()+'/bundle.html'); await p.waitForTimeout(5000);
 await p.getByRole('button',{name:'Mobil',exact:true}).click(); await p.waitForTimeout(800);
 fs.writeFileSync('m_Start.html',await p.evaluate(()=>document.querySelector('[data-dc-tpl="13"]').outerHTML));
 await p.screenshot({path:'m_top.png'});
 await p.getByRole('button',{name:'Menü'}).click().catch(e=>console.log('nomenu')); await p.waitForTimeout(500);
 await p.screenshot({path:'m_menu.png'});
 await b.close();
})();
