const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1440,height:900}});
 await p.goto('file://'+process.cwd()+'/bundle.html'); await p.waitForTimeout(5000);
 const btns=await p.$$('button[aria-expanded]');
 for(const bt of btns){ if(await bt.getAttribute('aria-expanded')==='false'){await bt.click(); await p.waitForTimeout(200);} }
 const out=await p.evaluate(()=>[...document.querySelectorAll('button[aria-expanded]')].map(b=>b.innerText.trim()+' => '+(b.closest('h3').nextElementSibling?.innerText||'')));
 console.log(out.join('\n'));
 const m=await b.newPage({viewport:{width:390,height:844}});
 await m.goto('file://'+process.cwd()+'/bundle.html'); await m.waitForTimeout(5000);
 await m.getByRole('button',{name:'Mobil',exact:true}).click(); await m.waitForTimeout(800);
 await m.screenshot({path:'m_start.png',fullPage:true});
 await b.close();
})();
