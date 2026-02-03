CREATE DATABASE IF NOT EXISTS rech00d;
USE rech00d;

CREATE TABLE domain (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) UNIQUE
);

CREATE TABLE recon_run (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  domain_id BIGINT,
  executed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (domain_id) REFERENCES domain(id)
);

CREATE TABLE subdomain (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  UNIQUE(name)
);

CREATE TABLE ip_address (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  ip VARCHAR(45),
  UNIQUE(ip)
);

CREATE TABLE recon_result (
  recon_id BIGINT,
  subdomain_id BIGINT,
  ip_id BIGINT,
  PRIMARY KEY (recon_id, subdomain_id),
  FOREIGN KEY (recon_id) REFERENCES recon_run(id),
  FOREIGN KEY (subdomain_id) REFERENCES subdomain(id),
  FOREIGN KEY (ip_id) REFERENCES ip_address(id)
);
