import mcp, json
SITE = 'https://newportfolio.digitalgrowthcatalyze.com'
FB = 'https://www.facebook.com/people/Digital-Growth-Catalyze/100095160666262/'
IG = 'https://www.instagram.com/digitalgrowthcatalyze/'
LI = 'https://www.linkedin.com/in/digital-growth-catalyze-8b8b28284/'
parts = mcp.call('elementor-list-site-parts', {})['result']
hdr = [p for p in parts if p.get('type') == 'header']
if hdr: pid = hdr[0]['post_id'] if 'post_id' in hdr[0] else hdr[0]['id']
else:
    r = mcp.call('elementor-manage-site-parts', {'operations': [{'action': 'create', 'type': 'header', 'title': 'DGC Header', 'conditions': ['include/general']}]})
    pid = r['results'][0]['id']
print('header post', pid)
X = '''<e-flexbox configuration-id="Site Header">
 <e-flexbox configuration-id="Top Bar">
  <e-flexbox configuration-id="Top Phone"><e-div-block configuration-id="Top Phone Icon"></e-div-block><e-paragraph configuration-id="Top Phone Text"></e-paragraph></e-flexbox>
  <e-flexbox configuration-id="Top Email"><e-div-block configuration-id="Top Email Icon"></e-div-block><e-paragraph configuration-id="Top Email Text"></e-paragraph></e-flexbox>
  <e-flexbox configuration-id="Top Follow">
   <e-paragraph configuration-id="Follow Label"></e-paragraph>
   <e-flexbox configuration-id="Top Facebook"><e-div-block configuration-id="Top Facebook Icon"></e-div-block></e-flexbox>
   <e-flexbox configuration-id="Top Instagram"><e-div-block configuration-id="Top Instagram Icon"></e-div-block></e-flexbox>
   <e-flexbox configuration-id="Top LinkedIn"><e-div-block configuration-id="Top LinkedIn Icon"></e-div-block></e-flexbox>
  </e-flexbox>
 </e-flexbox>
 <e-flexbox configuration-id="Main Nav">
  <e-image configuration-id="Logo"></e-image>
  <e-flexbox configuration-id="Nav Links">
   <e-button configuration-id="Link Portfolio"></e-button>
   <e-button configuration-id="Link Case Studies"></e-button>
   <e-button configuration-id="Link Video Reviews"></e-button>
  </e-flexbox>
  <e-flexbox configuration-id="Contact Button"><e-paragraph configuration-id="Contact Text"></e-paragraph><e-div-block configuration-id="Contact Arrow"></e-div-block></e-flexbox>
  <e-flexbox configuration-id="Menu Toggle"><e-div-block configuration-id="Menu Icon"></e-div-block></e-flexbox>
 </e-flexbox>
</e-flexbox>'''
link = lambda u, blank=False: {'destination': u, 'isTargetBlank': blank, 'tag': 'a'}
cfg = {
 'Site Header': {'tag': 'header'},
 'Top Phone': {'tag': 'a', 'link': link('tel:+18482062002')}, 'Top Phone Text': {'paragraph': '+1 848-206-2002', 'tag': 'span'},
 'Top Email': {'tag': 'a', 'link': link('mailto:info@digitalgrowthcatalyze.com')}, 'Top Email Text': {'paragraph': 'info@digitalgrowthcatalyze.com', 'tag': 'span'},
 'Follow Label': {'paragraph': 'Follow us :', 'tag': 'span'},
 'Top Facebook': {'tag': 'a', 'link': link(FB, True)}, 'Top Instagram': {'tag': 'a', 'link': link(IG, True)}, 'Top LinkedIn': {'tag': 'a', 'link': link(LI, True)},
 'Main Nav': {'tag': 'nav'},
 'Logo': {'image': {'src': {'id': 14}, 'size': 'full'}, 'link': link(SITE + '/')},
 'Link Portfolio': {'text': 'Portfolio', 'link': link(SITE + '/')},
 'Link Case Studies': {'text': 'Case Studies', 'link': link(SITE + '/case-studies/')},
 'Link Video Reviews': {'text': 'Video Reviews', 'link': link(SITE + '/video-reviews/')},
 'Contact Button': {'tag': 'a', 'link': link('https://digitalgrowthcatalyze.com/contact-us/')},
 'Contact Text': {'paragraph': 'Contact Us', 'tag': 'span'},
 'Menu Toggle': {'tag': 'button'},
}
classes = {
 'Site Header': ['dgc-hdr'], 'Top Bar': ['dgc-hdr-top'],
 'Top Phone': ['dgc-toplink'], 'Top Email': ['dgc-toplink', 'dgc-hide-mobile'], 'Top Follow': ['dgc-hide-mobile'],
 'Top Phone Icon': ['ico-phone'], 'Top Email Icon': ['ico-mail'],
 'Top Facebook': ['dgc-toplink'], 'Top Instagram': ['dgc-toplink'], 'Top LinkedIn': ['dgc-toplink'],
 'Top Facebook Icon': ['ico-facebook'], 'Top Instagram Icon': ['ico-instagram'], 'Top LinkedIn Icon': ['ico-linkedin'],
 'Main Nav': ['dgc-nav'], 'Nav Links': ['dgc-navlinks'],
 'Link Portfolio': ['dgc-navlink'], 'Link Case Studies': ['dgc-navlink'], 'Link Video Reviews': ['dgc-navlink'],
 'Contact Button': ['dgc-btn-hot', 'dgc-hide-tablet'], 'Contact Arrow': ['ico-arrow-right'],
 'Menu Toggle': ['dgc-burger'], 'Menu Icon': ['ico-burger'],
}
style = {
 'Top Email': 'justify-self: center;',
 'Top Follow': 'justify-self: end; align-items: center; gap: 14px; width: auto; padding: 0;',
 'Top Phone': 'justify-self: start; @media(--mobile) { justify-self: center; }',
 'Logo': 'height: 48px; width: auto; @media(--mobile) { height: 40px; }',
 'Contact Arrow': 'width: 18px; height: 18px;',
 'Menu Icon': 'width: 22px; height: 22px;',
}
r = mcp.call('elementor-build-composition', {'post_id': pid, 'xml_structure': X, 'element_config': cfg, 'classes': classes, 'style': style, 'parent_id': 'document', 'mode': 'replace_children'})
print(json.dumps({k: r.get(k) for k in ('success', 'warnings', 'root_element_ids')})[:1500])
pub = mcp.call('elementor-publish-document', {'post_id': pid}); print(json.dumps(pub)[:300])
json.dump({'header': pid}, open('parts.json', 'w'))
