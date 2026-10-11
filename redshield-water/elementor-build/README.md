# RedShield Water: Elementor build scripts

Builds the 13 RedShield Water pages plus header and footer on redshieldwater.emmenntech.com
through the Elementor MCP server (`/wp-json/elementor/mcp/`). Content and design match `../index.html`.

    export RS_MCP_AUTH="Basic <base64 of username:application-password>"
    python3 pages.py home          # or: about services pricing areas faqs tutorials contact
                                   #     leeds harrogate yorkshire ldu bds header footer
    python3 pages.py home --dry    # validate only, saves nothing

Page IDs: home 27, about 28, services 29, pricing 30, areas 31, faqs 32, tutorials 33, contact 34,
leeds 35, harrogate 36, yorkshire 37, ldu 38, bds 39; header 40, footer 41.
Images load from jsDelivr at the commit in `rsw/sha`.
After each build, `refresh_css` re-saves the first section through manage-elements, because
Elementor only regenerates a page's cached CSS on that save path.
