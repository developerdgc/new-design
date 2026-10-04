const I={
 check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20 6 9 17l-5-5"/></svg>',
 arrow:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 arrowUR:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17 17 7M8 7h9v9"/></svg>',
 plus:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 5v14M5 12h14"/></svg>',
 play:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg>',
 mail:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 phone:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 pin:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
 clock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
 target:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>',
 eye:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
 seo:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m20 20-4.8-4.8M7.5 12l2-2 1.5 1.5L14 8.5"/></svg>',
 local:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><path d="m9.5 9 1.8 1.8L15 7.2"/></svg>',
 ads:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11v2a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1z"/><path d="M15 9a4 4 0 0 1 0 6M18 6a8 8 0 0 1 0 12"/></svg>',
 web:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M9 9l-2 2 2 2M15 9l2 2-2 2"/></svg>',
 social:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="18" cy="5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="m8.2 10.8 7.6-4.4M8.2 13.2l7.6 4.4"/></svg>',
 ai:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>',
 shield:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>',
 fb:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8.5c0-.3.2-.5.5-.5z"/></svg>',
 ig:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/></svg>',
 li:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 9h4v12H4zM6 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v1.7c.6-1 1.9-2 3.8-2C21 8.7 22 10.6 22 14v7h-4v-6.3c0-1.6-.5-2.7-1.9-2.7-1.5 0-2.1 1.1-2.1 2.7V21h-4z"/></svg>',
 yt:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-3.8 31 31 0 0 0-.4-3.8zM10 15V9l5.2 3z"/></svg>'
};

const SVC=[
 {id:'seo',name:'SEO',ico:'seo',img:'{{img:s-seo}}',short:'Improve your visibility in Google and attract people actively searching for your products or services.',
  head:'SEO That Turns Searches Into Customers',
  intro:'We improve the pages, content and technical health of your website so Google understands what you offer, and the right people find you when they search.',
  feats:[['Technical SEO','Site speed, indexing, crawl errors and Core Web Vitals fixed first.'],['On-page optimisation','Titles, headings and content written around real search terms.'],['Content that ranks','Service and location pages built for buyer-intent keywords.'],['Authority building','Quality backlinks and mentions from relevant websites.']],
  probs:['Website not showing on page one','Traffic that never turns into leads','Competitors outranking you','No idea which keywords matter','Slow or broken pages','Reports full of jargon']},
 {id:'local-seo',name:'Local SEO',ico:'local',img:'{{img:s-gbp}}',short:'Improve your Google Business Profile, local rankings, citations, and visibility in Google Maps.',
  head:'Get Found in Google Maps and Local Search',
  intro:'For businesses that serve a city or region, the map pack is where calls come from. We optimise your Google Business Profile, citations and reviews so you show up there.',
  feats:[['Google Business Profile','Categories, services, photos and posts kept complete and active.'],['Citations','Consistent name, address and phone across directories.'],['Review strategy','A simple system to earn and reply to more reviews.'],['Local landing pages','Pages for each service area you want to rank in.']],
  probs:['Not appearing in the map pack','Few or old Google reviews','Wrong details on directories','Calls going to competitors','Multiple locations to manage','Unclear service areas']},
 {id:'google-ads',name:'Google Ads',ico:'ads',img:'{{img:s-landing}}',short:'Reach potential customers who are already searching for what you offer and optimize campaigns around leads and sales.',
  head:'Google Ads Built Around Leads, Not Clicks',
  intro:'We set up and manage Search, Performance Max and call campaigns with proper conversion tracking, so every dollar is measured against real leads and sales.',
  feats:[['Campaign structure','Tight ad groups matched to the services you sell.'],['Conversion tracking','Calls, forms and purchases tracked correctly.'],['Ad copy & landing pages','Messages and pages that match what people searched.'],['Ongoing optimisation','Weekly bid, keyword and negative keyword work.']],
  probs:['High cost per lead','Clicks with no calls','Broken or missing tracking','Wasted spend on wrong searches','No clear reporting','Agency lock-in contracts']},
 {id:'web',name:'Website Development',ico:'web',img:'{{img:s-webdev}}',short:'Build or improve a fast, mobile-friendly website that clearly communicates your offer and makes it easier for visitors to contact you.',
  head:'Websites That Make It Easy to Contact You',
  intro:'We design and build fast, mobile-first websites on WordPress and modern stacks, with clear messaging and conversion paths that turn visitors into enquiries.',
  feats:[['Conversion-focused design','Clear offer, trust signals and calls to action on every page.'],['Fast & mobile-first','Built to load quickly on any phone.'],['SEO-ready build','Clean structure, schema and on-page basics from day one.'],['Easy to update','A CMS your team can edit without a developer.']],
  probs:['Outdated or slow website','Visitors leave without contacting','Hard to update content','Not mobile friendly','Unclear services and pricing','No tracking on forms']},
 {id:'social',name:'Social Media Marketing',ico:'social',img:'{{img:s-social}}',short:'Create and manage content that keeps your business visible and helps you reach potential customers across major social platforms.',
  head:'Social Media That Keeps You Visible',
  intro:'We plan, create and publish content across Facebook, Instagram, LinkedIn and TikTok, and run paid social campaigns when you want to reach new audiences.',
  feats:[['Content calendar','A monthly plan built around your services and seasons.'],['Creative production','Graphics, short videos and captions in your brand style.'],['Community management','Comments and messages answered on time.'],['Paid social','Meta and LinkedIn campaigns for leads and retargeting.']],
  probs:['Inconsistent posting','No time to create content','Low engagement','Followers that never become customers','Off-brand visuals','No reporting']},
 {id:'ai-search',name:'AI Search Optimization',ico:'ai',img:'{{img:hero-bg}}',short:"Improve your online presence for AI-powered search and answer engines, including Google's AI search features and other AI platforms.",
  head:'Get Recommended by AI Search',
  intro:"People now ask ChatGPT, Perplexity and Google's AI features for recommendations. We structure your content and brand signals so these tools understand and cite your business.",
  feats:[['Entity & schema','Structured data that clearly describes your business.'],['Answer-ready content','Clear answers to the questions customers ask.'],['Brand mentions','Consistent presence on the sources AI tools trust.'],['AI visibility tracking','Monitoring where and how you are mentioned.']],
  probs:['Not mentioned in AI answers','Competitors cited instead of you','Thin or unclear service content','Missing structured data','Inconsistent brand info online','No way to measure AI visibility']}
];
const WHY=[['Clear Strategy','We focus on what your business actually needs. Every plan starts from your goals, customers and current online presence.'],['Practical Execution','We handle the work, not just the planning. Our team implements the SEO, ads and website changes ourselves.'],['Business-Focused','Our goal is more leads, customers, and sales, not just traffic. We report on calls, forms and revenue.'],['Transparent Reporting','See exactly what we’re doing and the results we’re getting, in plain language, every month.']];
const STEPS=[['Understand','We learn about your business, goals, customers, and current online presence.'],['Plan','We identify what needs improvement and create a practical strategy.'],['Execute','We do the agreed work and keep you informed throughout the process.'],['Improve','We review the data, identify what is working, and make improvements over time.']];
const PLAT=[['G','Google Search','Organic SEO','#2F7BEA'],['GB','Business Profile','Maps & local','#0B4FB0'],['Ads','Google Ads','Paid search','#E2A400'],['GA4','Analytics 4','Tracking','#E8710A'],['f','Meta','Facebook & Instagram','#1877F2'],['in','LinkedIn','B2B social','#0A66C2'],['Tk','TikTok','Short video','#111827'],['WP','WordPress','Websites','#21759B']];
const VIDS=[
 {id:'fV2UIO6vWaM',t:'“They explained everything in plain language”',s:'Client video review',img:'{{v_fV2UIO6vWaM}}'},
 {id:'LByRG9RuCSY',t:'Working with EmmEnn Tech on SEO',s:'Client video review',img:'{{v_LByRG9RuCSY}}'},
 {id:'uLUuJYvsjco',t:'More enquiries from our website',s:'Client video review',img:'{{v_uLUuJYvsjco}}'},
 {id:'0HTQh_vvbmc',t:'Quick review from a happy client',s:'YouTube Short',img:'{{v_0HTQh_vvbmc}}',short:true}
];
const TST=[
 ['Yusuf was easy to work with from the start. He understood what we needed, explained the strategy clearly, and kept us updated throughout the project.','London, UK'],
 ['We hired EmmEnn Tech for SEO and website improvements. The communication was straightforward, and Yusuf always explained what was being done instead of using complicated marketing language.','New York, USA'],
 ['Yusuf and his team handled our digital marketing professionally. We had a clear plan from the beginning and could see what work was being completed each month.','Virginia, USA'],
 ['Working with EmmEnn Tech has been a good experience. Yusuf is responsive, practical, and focused on solving the actual problems instead of making big promises.','California, USA'],
 ['We needed help improving our online presence and generating more enquiries. Yusuf took the time to understand our business and gave us a clear plan to work with.','Maryland, USA'],
 ['Our Google Business Profile finally shows up in the map pack for our main service. The monthly reports make it easy to see what changed.','Denver, USA']
];
const PLANS=[
 {n:'Starter',f:'Local businesses getting found',m:499,y:399,items:['Google Business Profile optimisation','Local citations (30 / month)','2 local landing pages','Review growth system','Monthly report']},
 {n:'Growth',f:'Businesses ready to scale leads',m:999,y:799,hot:true,items:['Everything in Starter','Full SEO (technical + content)','Google Ads management','Call & form tracking','Bi-weekly check-in call']},
 {n:'Scale',f:'Multi-channel, multi-location',m:1999,y:1599,items:['Everything in Growth','AI search optimization','Social media management','Landing page CRO','Dedicated account manager']}
];
const FAQ=[
 ['How long does SEO take to show results?','Most clients see early movement in rankings within 6–12 weeks. Steady growth in leads usually comes between months 3 and 6, depending on competition.'],
 ['Do you require long-term contracts?','No. Our monthly plans run month to month after the first 3 months, so you stay because it works.'],
 ['What do your monthly reports include?','Work completed, rankings, traffic, calls, form leads and ad spend, plus what we plan to do next. Written in plain language.'],
 ['Do you work with businesses outside the US?','Yes. We work with clients in the US, UK and other markets, and schedule calls around your time zone.'],
 ['Can you work on my existing website?','Yes. We can improve your current site or rebuild it if that is the better option. We’ll tell you honestly which one makes sense.'],
 ['How much should I spend on Google Ads?','It depends on your market and cost per click. We start with a test budget, track leads, and scale what is profitable.']
];
const WORKS=[
 ['Web Conversion Architecture','Web','{{p2}}'],['SEO Generative Visibility','SEO','{{p1}}'],['Ads Targeted Reach','Ads','{{p4}}'],
 ['Analytics Dashboard UI','Web','{{p3}}'],['Social Brand Engagement','Social','{{p5}}'],['Growth Reporting Suite','SEO','{{p6}}'],['Command Center Reporting','Ads','{{p7}}'],['Mobile-First Rebuild','Web','{{img:s-webdev}}'],['Instagram Content System','Social','{{img:s-social}}']
];
const CASES=[
 ['Home services, Denver','Faster replies turned searches into booked jobs','Avg. response time','4 hours','2 minutes','30x faster','{{img:s-reviews}}'],
 ['Dental clinic, Virginia','Map pack rankings for every core service','Calls from Maps / month','38','112','+195%','{{img:s-gbp}}'],
 ['E-commerce, California','Cheaper leads and a fuller pipeline','Cost per lead','$96','$57','-41%','{{img:s-ecom}}']
];

