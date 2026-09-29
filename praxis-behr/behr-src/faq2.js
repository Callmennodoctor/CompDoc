const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1440,height:900}});
 await p.goto('file://'+process.cwd()+'/bundle.html'); await p.waitForTimeout(5000);
 const n=await p.$$eval('button[aria-expanded]',x=>x.length);
 for(let i=0;i<n;i++){
   const bt=(await p.$$('button[aria-expanded]'))[i];
   if(await bt.getAttribute('aria-expanded')==='false'){await bt.click(); await p.waitForTimeout(250);}
   const t=await p.evaluate(i=>{const b=document.querySelectorAll('button[aria-expanded]')[i];return b.innerText.trim()+' => '+(b.closest('h3').nextElementSibling?.innerText||'')},i);
   console.log(t);
 }
 await b.close();
})();
