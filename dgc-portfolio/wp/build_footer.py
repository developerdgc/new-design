import mcp, json
C = {
 'dgc-ftr': 'flex-direction: column; padding: 70px 16px 0; gap: 0; color: #ffffff; font-family: Poppins; background: radial-gradient(70% 45% at 50% 0%, rgba(28,222,225,0.28), transparent 70%), radial-gradient(70% 50% at 50% 100%, rgba(28,222,225,0.3), transparent 70%), linear-gradient(180deg, #0c4a52 0%, #041b24 26%, #031820 62%, #0c4d55 100%);',
 'dgc-ftr-wrap': 'flex-direction: column; gap: 0; max-width: 1260px; width: 100%; margin: 0 auto; padding: 0;',
 'dgc-ftr-grid': 'grid-template-columns: 1.3fr 0.8fr 1fr 1.35fr; grid-template-rows: auto; gap: 40px; align-items: start; padding: 0; @media(--tablet) { grid-template-columns: 1fr 1fr; } @media(--mobile) { grid-template-columns: 1fr; gap: 34px; }',
 'dgc-ftr-col': 'flex-direction: column; align-items: flex-start; gap: 0; padding: 0;',
 'dgc-ftr-about': 'padding-top: 34px; @media(--tablet) { padding-top: 0; }',
 'dgc-ftr-h': 'font-family: Poppins; font-size: 1.65rem; font-weight: 500; line-height: 1.3; color: var(--orange); text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 5px; margin-bottom: 34px; @media(--mobile) { font-size: 1.4rem; margin-bottom: 20px; }',
 'dgc-ftr-list': 'flex-direction: column; align-items: flex-start; gap: 22px; padding: 0; @media(--mobile) { gap: 14px; }',
 'dgc-ftr-link': 'display: inline-flex; align-items: center; gap: 10px; width: auto; padding: 0; color: #ffffff; font-size: 1.05rem; text-decoration: none; transition: color 0.25s, gap 0.25s; &:hover { color: var(--orange); gap: 14px; }',
 'dgc-dash': 'width: 12px; height: 2px; min-width: 0; padding: 0; flex: none; border-radius: 2px; background: currentColor;',
 'dgc-ftr-p': 'font-family: Poppins; font-size: 1rem; line-height: 1.55; color: #ffffff; max-width: 40ch; margin-top: 22px;',
 'dgc-ftr-soc': 'gap: 14px; width: auto; padding: 0; margin-top: 26px;',
 'dgc-ftr-socbtn': 'display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; padding: 0; border-radius: 10px; color: #ffffff; transition: background 0.25s, color 0.25s; &:hover { background: var(--orange); color: var(--abyss); }',
 'dgc-ftr-contact': 'flex-direction: column; align-items: flex-start; gap: 18px; padding: 0; margin-top: 4px;',
 'dgc-ftr-crow': 'align-items: flex-start; gap: 10px; width: auto; padding: 0; color: #ffffff; font-size: 1.05rem; line-height: 1.45; text-decoration: none; transition: color 0.25s; &:hover { color: var(--orange); }',
 'dgc-ftr-h5': 'font-family: Poppins; font-size: 1.55rem; font-weight: 500; color: #ffffff; margin: 30px 0 14px;',
 'dgc-ftr-base': 'width: 100%; margin-top: 56px; padding: 26px 0 30px; border-top: 1px solid rgba(255,255,255,0.85); text-align: center; font-family: Poppins; font-size: 1.05rem; color: #ffffff;',
 'dgc-totop': 'position: fixed; right: 26px; bottom: 26px; z-index: 90; display: flex; align-items: center; justify-content: center; width: 46px; height: 46px; min-width: 0; padding: 0; border: 2px solid #ffffff; border-radius: 50%; background: var(--orange); color: #ffffff; cursor: pointer; box-shadow: 0 10px 24px -8px rgba(0,0,0,0.5); opacity: 0; transform: translateY(12px); pointer-events: none; transition: opacity 0.3s, transform 0.3s, background 0.25s, color 0.25s; &:hover { background: #ffffff; color: var(--orange); } @media(--mobile) { right: 16px; bottom: 16px; }',
}
r = mcp.call('elementor-manage-classes', {'operations': [{'action': 'create', 'label': k, 'css': v} for k, v in C.items()]})
print('classes', [(x.get('label'), x.get('error')) for x in r['results'] if x['status'] != 'ok'] or 'ok')

M = 'https://digitalgrowthcatalyze.com'
QUICK = [('/', 'Home'), ('/about-us/', 'About Us'), ('/our-services/', 'Our Services'), ('/blog/', 'Our Blog'), ('/contact-us/', 'Contact Us'), ('/privacy-policy/', 'Privacy Policy'), ('/refund-policy/', 'Refund Policy')]
SERV = [('/ai-geo-optimization/', 'AI &amp; GEO Optimization'), ('/google-business-profile/', 'Google Business Profile'), ('/seo-services/', 'SEO Services'), ('/google-ads-lsa/', 'Google Ads &amp; LSA'), ('/website-development/', 'Website Development'), ('/social-media-marketing/', 'Social Media Marketing')]
link = lambda u, blank=False: {'destination': u, 'isTargetBlank': blank, 'tag': 'a'}
cfg, cls, sty = {}, {}, {}
def links(prefix, items):
    x = ''
    for i, (path, label) in enumerate(items):
        k = f'{prefix} {i + 1}'
        x += f'<e-flexbox configuration-id="{k}"><e-div-block configuration-id="{k} Dash"></e-div-block><e-paragraph configuration-id="{k} Text"></e-paragraph></e-flexbox>'
        cfg[k] = {'tag': 'a', 'link': link(M + path)}; cls[k] = ['dgc-ftr-link']; cls[k + ' Dash'] = ['dgc-dash']
        cfg[k + ' Text'] = {'paragraph': label.replace('&amp;', '&'), 'tag': 'span'}
    return x
FB = 'https://www.facebook.com/people/Digital-Growth-Catalyze/100095160666262/'
IG = 'https://www.instagram.com/digitalgrowthcatalyze/'
LI = 'https://www.linkedin.com/in/digital-growth-catalyze-8b8b28284/'
X = f'''<e-flexbox configuration-id="Site Footer"><e-flexbox configuration-id="Footer Wrap">
 <e-grid configuration-id="Footer Grid">
  <e-flexbox configuration-id="Col About">
   <e-image configuration-id="Footer Logo"></e-image>
   <e-paragraph configuration-id="About Text"></e-paragraph>
   <e-flexbox configuration-id="Footer Social">
    <e-flexbox configuration-id="Social Facebook"><e-div-block configuration-id="Social Facebook Icon"></e-div-block></e-flexbox>
    <e-flexbox configuration-id="Social Instagram"><e-div-block configuration-id="Social Instagram Icon"></e-div-block></e-flexbox>
    <e-flexbox configuration-id="Social LinkedIn"><e-div-block configuration-id="Social LinkedIn Icon"></e-div-block></e-flexbox>
   </e-flexbox>
  </e-flexbox>
  <e-flexbox configuration-id="Col Quick"><e-heading configuration-id="Quick Heading"></e-heading><e-flexbox configuration-id="Quick List">{links('Quick', QUICK)}</e-flexbox></e-flexbox>
  <e-flexbox configuration-id="Col Services"><e-heading configuration-id="Services Heading"></e-heading><e-flexbox configuration-id="Services List">{links('Service', SERV)}</e-flexbox></e-flexbox>
  <e-flexbox configuration-id="Col Contact">
   <e-heading configuration-id="Contact Heading"></e-heading>
   <e-flexbox configuration-id="Contact List">
    <e-flexbox configuration-id="Address Row"><e-div-block configuration-id="Address Icon"></e-div-block><e-paragraph configuration-id="Address Text"></e-paragraph></e-flexbox>
    <e-flexbox configuration-id="Phone Row"><e-div-block configuration-id="Phone Icon"></e-div-block><e-paragraph configuration-id="Phone Text"></e-paragraph></e-flexbox>
    <e-flexbox configuration-id="Email Row"><e-div-block configuration-id="Email Icon"></e-div-block><e-paragraph configuration-id="Email Text"></e-paragraph></e-flexbox>
   </e-flexbox>
   <e-heading configuration-id="Accept Heading"></e-heading>
   <e-image configuration-id="Payment Logos"></e-image>
  </e-flexbox>
 </e-grid>
 <e-paragraph configuration-id="Copyright"></e-paragraph>
</e-flexbox>
<e-flexbox configuration-id="Back To Top"><e-div-block configuration-id="Back To Top Icon"></e-div-block></e-flexbox>
</e-flexbox>'''
cfg.update({
 'Site Footer': {'tag': 'footer'},
 'Footer Logo': {'image': {'src': {'id': 14}, 'size': 'full'}, 'link': link(M + '/')},
 'About Text': {'paragraph': 'At Digital Growth Catalyze LLC our aim is to assist the small and medium-sized businesses to grow online. DGC is a world-class digital marketing agency with over 17 years of experience.'},
 'Social Facebook': {'tag': 'a', 'link': link(FB, True)}, 'Social Instagram': {'tag': 'a', 'link': link(IG, True)}, 'Social LinkedIn': {'tag': 'a', 'link': link(LI, True)},
 'Quick Heading': {'tag': 'h4', 'title': 'Quick Link'}, 'Services Heading': {'tag': 'h4', 'title': 'Services'}, 'Contact Heading': {'tag': 'h4', 'title': 'Contact Us'},
 'Address Text': {'paragraph': 'JACKSON HEIGHTS,<br>New York 11372', 'tag': 'span'},
 'Phone Row': {'tag': 'a', 'link': link('tel:+18482062002')}, 'Phone Text': {'paragraph': '+1 848-206-2002', 'tag': 'span'},
 'Email Row': {'tag': 'a', 'link': link('mailto:info@digitalgrowthcatalyze.com')}, 'Email Text': {'paragraph': 'info@digitalgrowthcatalyze.com', 'tag': 'span'},
 'Accept Heading': {'tag': 'h5', 'title': 'We Accept'},
 'Payment Logos': {'image': {'src': {'id': 11}, 'size': 'full'}},
 'Copyright': {'paragraph': '2009-2026 © Copyrights Digital Growth Catalyze. All rights reserved.'},
 'Back To Top': {'tag': 'button'},
})
cls.update({
 'Site Footer': ['dgc-ftr'], 'Footer Wrap': ['dgc-ftr-wrap'], 'Footer Grid': ['dgc-ftr-grid'],
 'Col About': ['dgc-ftr-col', 'dgc-ftr-about'], 'Col Quick': ['dgc-ftr-col'], 'Col Services': ['dgc-ftr-col'], 'Col Contact': ['dgc-ftr-col'],
 'About Text': ['dgc-ftr-p'], 'Footer Social': ['dgc-ftr-soc'],
 'Social Facebook': ['dgc-ftr-socbtn'], 'Social Instagram': ['dgc-ftr-socbtn'], 'Social LinkedIn': ['dgc-ftr-socbtn'],
 'Social Facebook Icon': ['ico-facebook'], 'Social Instagram Icon': ['ico-instagram'], 'Social LinkedIn Icon': ['ico-linkedin'],
 'Quick Heading': ['dgc-ftr-h'], 'Services Heading': ['dgc-ftr-h'], 'Contact Heading': ['dgc-ftr-h'],
 'Quick List': ['dgc-ftr-list'], 'Services List': ['dgc-ftr-list'], 'Contact List': ['dgc-ftr-contact'],
 'Address Row': ['dgc-ftr-crow'], 'Phone Row': ['dgc-ftr-crow'], 'Email Row': ['dgc-ftr-crow'],
 'Address Icon': ['ico-pin'], 'Phone Icon': ['ico-phone'], 'Email Icon': ['ico-mail'],
 'Accept Heading': ['dgc-ftr-h5'], 'Copyright': ['dgc-ftr-base'],
 'Back To Top': ['dgc-totop'], 'Back To Top Icon': ['ico-chevron-up'],
})
sty.update({
 'Footer Logo': 'height: 62px; width: auto;',
 'Social Facebook Icon': 'width: 22px; height: 22px;', 'Social Instagram Icon': 'width: 22px; height: 22px;', 'Social LinkedIn Icon': 'width: 22px; height: 22px;',
 'Address Icon': 'margin-top: 4px;', 'Phone Icon': 'margin-top: 4px;', 'Email Icon': 'margin-top: 4px;',
 'Email Text': 'white-space: nowrap; @media(--mobile) { white-space: normal; overflow-wrap: anywhere; }',
 'Payment Logos': 'height: 30px; width: auto;',
 'Back To Top Icon': 'width: 22px; height: 22px;',
})
parts = mcp.call('elementor-list-site-parts', {})['result']
ftr = [p for p in parts if p.get('type') == 'footer']
if ftr: pid = ftr[0].get('post_id') or ftr[0].get('id')
else: pid = mcp.call('elementor-manage-site-parts', {'operations': [{'action': 'create', 'type': 'footer', 'title': 'DGC Footer', 'conditions': ['include/general']}]})['results'][0]['id']
print('footer post', pid)
r = mcp.call('elementor-build-composition', {'post_id': pid, 'xml_structure': X, 'element_config': cfg, 'classes': cls, 'style': sty, 'parent_id': 'document', 'mode': 'replace_children'})
print(json.dumps({k: r.get(k) for k in ('success', 'warnings', 'root_element_ids')})[:1500])
print(json.dumps(mcp.call('elementor-publish-document', {'post_id': pid}))[:200])
d = json.load(open('parts.json')); d['footer'] = pid; json.dump(d, open('parts.json', 'w'))
