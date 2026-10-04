# Store policies (paste into Shopify admin)

The Shopify connector has no `write_legal_policies` scope, so these must be pasted manually:
Shopify admin → Settings → Policies → open the policy → click the `<>` (Show HTML) button in the editor → paste the file contents → Save.

| File | Shopify policy | Source |
|---|---|---|
| `terms-of-service.html` | Terms of service | Client text, word for word from `source-docs/brief-Share_w_Ali.pdf` (only formatted) |
| `shipping-policy.html` | Shipping policy | Client text from the PDF; "quicker then" corrected to "quicker than" |
| `refund-policy_DRAFT.html` | Return and refund policy | **Drafted by Claude**. Client has not supplied one. Covers Australian Consumer Law rights and damaged/faulty items only. **Change-of-mind returns are intentionally not covered: the client must decide** (e.g. originals within X days? prints made to order excluded?). |

Notes
- The Terms use "Kylie Washington Studios" (with s) while the site title is "Kylie Washington Studio". Left as the client wrote it; ask which is the legal/trading name.
- Terms section 4 says the edition size of limited edition prints "will be specified in the product description". Edition sizes are not on the products yet.
- Privacy policy: Shopify's generated template already exists.
