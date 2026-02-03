import glob, csv, mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="rech00d",
  password="rech00d",
  database="rech00d"
)
c = db.cursor()

files = glob.glob("output/resolved/*.csv")

for f in files:
  with open(f) as file:
    reader = csv.reader(file)
    for domain, sub, ip, ts in reader:
      c.execute("INSERT IGNORE INTO domain(name) VALUES(%s)", (domain,))
      c.execute("SELECT id FROM domain WHERE name=%s", (domain,))
      domain_id = c.fetchone()[0]

      c.execute("INSERT INTO recon_run(domain_id) VALUES(%s)", (domain_id,))
      recon_id = c.lastrowid

      c.execute("INSERT IGNORE INTO subdomain(name) VALUES(%s)", (sub,))
      c.execute("SELECT id FROM subdomain WHERE name=%s", (sub,))
      sub_id = c.fetchone()[0]

      c.execute("INSERT IGNORE INTO ip_address(ip) VALUES(%s)", (ip,))
      c.execute("SELECT id FROM ip_address WHERE ip=%s", (ip,))
      ip_id = c.fetchone()[0]

      c.execute("""
        INSERT IGNORE INTO recon_result
        VALUES (%s,%s,%s)
      """, (recon_id, sub_id, ip_id))

db.commit()
print("[+] Dados persistidos")
