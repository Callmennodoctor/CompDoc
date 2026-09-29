const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
 const b=await chromium.launch();
 for (const [name,vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]){
  const p=await b.newPage({viewport:vp});
  p.on('console',m=>{if(m.type()==='error')console.log('ERR',m.text().slice(0,200))});
  await p.goto('file://'+process.cwd()+'/bundle.html');
  await p.waitForTimeout(6000);
  await p.screenshot({path:`${name}.png`,fullPage:true});
  if(name==='desktop'){ require('fs').writeFileSync('rendered.html', await p.content()); }
  const h=await p.evaluate(()=>document.body.scrollHeight); console.log(name,h);
 }
 await b.close();
})();
