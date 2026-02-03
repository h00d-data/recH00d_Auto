import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="rech00d",
  password="rech00d",
  database="rech00d"
)
c = db.cursor()

c.execute("""
SELECT d.name, COUNT(r.subdomain_id)
FROM recon_result r
JOIN recon_run rr ON r.recon_id=rr.id
JOIN domain d ON rr.domain_id=d.id
GROUP BY d.name
""")

html = "<h1>RecH00D Report</h1><ul>"
for row in c.fetchall():
  html += f"<li>{row[0]}: {row[1]} subdomínios</li>"
html += "</ul>"

open("output/reports/report.html","w").write(html)
