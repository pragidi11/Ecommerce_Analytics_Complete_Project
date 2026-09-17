# Commerce IQ — compatibility edition

Four-page native Power BI project with embedded sample data, a star schema and 12 DAX measures. This edition stores the report in a single PBIR-Legacy `report.json`, using serialized queries, visual bindings and projection metadata modeled on Microsoft’s public Performance Analyzer sample. It avoids the enhanced PBIR folder loader.

## Open

Extract into a new folder and open `CommerceIQ_Compatibility.pbip`. Four named page tabs should appear. Refresh the embedded data and save as PBIX in Power BI Desktop. Keep both item folders alongside the PBIP file.

## Status

This is a compatibility repair candidate. The prior enhanced-format report appeared blank on the user's desktop. The uploaded archive was byte-for-byte identical to the original and did not include the Desktop-saved output, so the root cause remains unconfirmed. The legacy report format is not a publicly documented external-authoring schema; runtime behavior must be validated in Desktop. The environment used to create this package cannot run Desktop. No successful runtime rendering or DAX execution is claimed.

## Data

The original sample model is unchanged. Eligible net revenue: $17,262,114.33; distinct eligible orders: 18,035; distinct purchasing customers: 4,857. Cancelled and refunded orders are excluded. All other source statuses remain included. Revenue excludes shipping and tax. The embedded snapshot spans January 1, 2025 through September 13, 2026. Refresh reloads that snapshot, not new upstream transactions.

Customer lifetime value ignores calendar and category selections while retaining customer context. Date/state/category slicers are configured to sync across pages. These settings require Desktop verification.

## References

- https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report
- https://github.com/microsoft/powerbi-desktop-samples/tree/main/Performance%20Analyzer

Upload the complete project to GitHub after Desktop validation; optionally include the resulting PBIX and genuine screenshots.
