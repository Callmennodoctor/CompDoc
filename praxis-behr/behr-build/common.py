# Shared design tokens and CSS for Praxis Behr Webflow build
INK="#1B2540"; PAPER="#FAFBFD"; GRID="#CBD8E8"; BLUE="#2F5BA8"; GREEN="#4E9A68"; VIOLET="#6A47A0"; MARK="#F2EA4A"
HF="Gabarito, system-ui, sans-serif"; BF="'Atkinson Hyperlegible Next', system-ui, sans-serif"
PADX="clamp(20px, 5vw, 80px)"
MARKBG=f"linear-gradient(transparent 12%, {MARK} 12%, {MARK} 88%, transparent 88%)"
SM="@media screen and (max-width: 767px)"
TAB="@media screen and (max-width: 991px)"

def m(t, extra=""):
    return f'<span class="bh-mark{extra}">{t}</span>'

BASE_CSS = f"""
.bh-sec{{font-family:{BF};font-size:1.125rem;line-height:1.55;color:{INK};background-color:{PAPER};padding-top:clamp(72px,9vw,128px);padding-right:{PADX};padding-bottom:0px;padding-left:{PADX}}}
.bh-mark{{background-image:{MARKBG};padding-right:0.18em;padding-left:0.18em;-webkit-box-decoration-break:clone;box-decoration-break:clone;color:{INK}}}
.bh-h1{{margin-top:40px;margin-bottom:0px;font-family:{HF};font-weight:700;font-size:clamp(2.4rem,3.3vw + 1rem,4.4rem);line-height:1.05;letter-spacing:-0.015em;text-wrap:balance;color:{INK}}}
.bh-h2{{margin-top:0px;margin-bottom:24px;font-family:{HF};font-weight:700;font-size:clamp(1.9rem,2vw + 1.2rem,2.75rem);line-height:1.1;text-wrap:balance;color:{INK}}}
.bh-h3{{margin-top:0px;margin-bottom:8px;font-family:{HF};font-weight:600;font-size:1.3125rem;line-height:1.25;color:{INK}}}
.bh-p{{margin-top:0px;margin-bottom:16px;max-width:62ch}}
.bh-lead{{margin-top:0px;margin-bottom:0px;max-width:56ch;font-size:1.25rem}}
.bh-btn{{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding-top:0px;padding-right:24px;padding-bottom:0px;padding-left:24px;background-color:{BLUE};color:{PAPER};border-top-left-radius:6px;border-top-right-radius:6px;border-bottom-left-radius:6px;border-bottom-right-radius:6px;font-family:{HF};font-weight:600;font-size:1.0625rem;text-decoration:none;font-variant-numeric:tabular-nums}}
.bh-btn:hover{{background-color:{INK};color:{PAPER}}}
.bh-btn:focus-visible{{outline-color:{BLUE};outline-width:2px;outline-style:solid;outline-offset:2px}}
.bh-tlink{{display:inline-flex;align-items:center;min-height:44px;font-family:{HF};font-weight:500;font-size:1.0625rem;color:{INK};text-decoration:underline;text-decoration-color:{BLUE};text-decoration-thickness:2px;text-underline-offset:0.25em}}
.bh-tlink:hover{{color:{BLUE}}}
.bh-tlink:focus-visible{{outline-color:{BLUE};outline-width:2px;outline-style:solid;outline-offset:2px}}
.bh-muted{{color:#48536B}}
.bh-label{{display:block;padding-top:14px;padding-right:18px;padding-bottom:14px;padding-left:18px;background-color:#FFFFFF;border-top:1.5px solid {INK};border-right:1.5px solid {INK};border-bottom:1.5px solid {INK};border-left:1.5px solid {INK};border-top-left-radius:4px;border-top-right-radius:4px;border-bottom-left-radius:4px;border-bottom-right-radius:4px}}
.bh-label-date{{margin-top:0px;margin-bottom:0px;font-size:0.875rem;font-variant-numeric:tabular-nums;color:#48536B}}
.bh-label-state{{margin-top:4px;margin-bottom:0px;font-family:{HF};font-weight:700;font-size:1.25rem;line-height:1.25}}
.bh-ph{{display:flex;align-items:center;justify-content:center;padding-top:24px;padding-right:24px;padding-bottom:24px;padding-left:24px;background-color:#EEF1F5;border-top:1px solid #9AA3B5;border-right:1px solid #9AA3B5;border-bottom:1px solid #9AA3B5;border-left:1px solid #9AA3B5;border-top-left-radius:4px;border-top-right-radius:4px;border-bottom-left-radius:4px;border-bottom-right-radius:4px;color:#48536B;font-size:0.9375rem;text-align:center}}
.bh-grid-bg{{background-image:linear-gradient(rgba(203,216,232,0.55) 1px, transparent 1px), linear-gradient(90deg, rgba(203,216,232,0.55) 1px, transparent 1px);background-size:5mm 5mm}}
"""
