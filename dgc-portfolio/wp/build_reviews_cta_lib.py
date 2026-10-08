import json
M = {k: v['id'] for k, v in json.load(open('media-map.json')).items()}
link = lambda u: {'destination': u, 'isTargetBlank': False, 'tag': 'a'}
def cta():
    XC = '''<e-flexbox configuration-id="CTA"><e-div-block configuration-id="CTA Wrap"><e-grid configuration-id="CTA Box">
     <e-image configuration-id="CTA Watermark"></e-image>
     <e-div-block configuration-id="CTA Copy"><e-paragraph configuration-id="CTA Kicker"></e-paragraph><e-heading configuration-id="CTA Title"></e-heading><e-paragraph configuration-id="CTA Text"></e-paragraph></e-div-block>
     <e-flexbox configuration-id="CTA Buttons">
      <e-flexbox configuration-id="CTA Quote"><e-paragraph configuration-id="CTA Quote Text"></e-paragraph><e-div-block configuration-id="CTA Quote Icon"></e-div-block></e-flexbox>
      <e-flexbox configuration-id="CTA Call"><e-paragraph configuration-id="CTA Call Text"></e-paragraph></e-flexbox>
     </e-flexbox>
    </e-grid></e-div-block></e-flexbox>'''
    cfgc = {'CTA': {'tag': 'section'}, 'CTA Watermark': {'image': {'src': {'id': M['img/brand/dgc-mark-white.png']}, 'size': 'full'}},
            'CTA Kicker': {'paragraph': 'Let’s grow together', 'tag': 'span'}, 'CTA Title': {'tag': 'h2', 'title': 'Ready for more calls?'},
            'CTA Text': {'paragraph': 'Website, SEO, Google Ads or all three. Tell us where you want to grow.'},
            'CTA Quote': {'tag': 'a', 'link': link('https://digitalgrowthcatalyze.com/contact-us/')}, 'CTA Quote Text': {'paragraph': 'Get a Free Quote', 'tag': 'span'},
            'CTA Call': {'tag': 'a', 'link': link('tel:+18482062002')}, 'CTA Call Text': {'paragraph': 'Call +1 848-206-2002', 'tag': 'span'}}
    clsc = {'CTA': ['dgc-cta'], 'CTA Wrap': ['dgc-wrap'], 'CTA Box': ['dgc-cta-box'], 'CTA Watermark': ['dgc-cta-mark'], 'CTA Kicker': ['dgc-kicker', 'dgc-kicker-navy'],
            'CTA Title': ['dgc-cta-h'], 'CTA Text': ['dgc-cta-p'], 'CTA Buttons': ['dgc-cta-btns'], 'CTA Quote': ['dgc-btn', 'dgc-btn-ink'], 'CTA Quote Icon': ['ico-arrow-ur'], 'CTA Call': ['dgc-btn', 'dgc-btn-line']}
    
    return dict(xml_structure=XC, element_config=cfgc, classes=clsc, style={'CTA Copy': 'padding: 0;'})
