from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def db():
  return mysql.connector.connect(
    host="localhost",
    user="rech00d",
    password="rech00d",
    database="rech00d"
  )

@app.route("/domains")
def domains():
  c = db().cursor()
  c.execute("SELECT name FROM domain")
  return jsonify([d[0] for d in c.fetchall()])

@app.route("/subdomains/<domain>")
def subs(domain):
  c = db().cursor()
  c.execute("""
    SELECT s.name, ip.ip
    FROM recon_result r
    JOIN recon_run rr ON r.recon_id=rr.id
    JOIN domain d ON rr.domain_id=d.id
    JOIN subdomain s ON r.subdomain_id=s.id
    JOIN ip_address ip ON r.ip_id=ip.id
    WHERE d.name=%s
  """,(domain,))
  return jsonify(c.fetchall())

app.run(host="0.0.0.0", port=8080)
