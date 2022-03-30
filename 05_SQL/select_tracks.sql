SELECT TrackId, SUM(UnitPrice) as TotalPrice, COUNT(*) as TotalRecords
FROM invoice_items
GROUP BY TrackId;