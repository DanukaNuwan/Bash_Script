#!/bin/bash 
# Define the target URL or IP address 
target="$1" 

# Define the output file 
output="result.txt" 

# Check if a target is provided as an argument 
if [ -z "$target”]; then 
echo "Usage: $0 <target>" 

exit 1 
fi 
# Create a timestamp for the log 
timestamp=$(date +"%Y-%m-%d %H: %M:%S") 

# Start scanning 
echo "Scanning $target at $timestamp" 


echo "=========START==========" 


# Find subdomains using amass. 
echo "Find subdomains using amass" 
amass enum -d "$target" >> "$output" 

echo "========================" 

# Port scan using Nmap 
echo "Port Scanning using Nmap." 
nmap -p- -T4 "$target" >> "$output" 

echo "==========================" 

# Reconnaissance tasks using Nikto 
echo "Reconnaissance using Nikto" >> "$output" 
nikto -h "$target" >> "$output" 

echo "==========================" 

# Scan WordPress/Silverstripe/Drupal sites using droopscan 
echo "Scan using droopscan" >> "$output" 
droopescan scan drupal -u "$target" >> "$output" 

echo "==========================" 

# Find emails and people names from Google using theHarvester 
echo "Scan using theHarvester" >> "$output" 
theHarvester -d "$target" -l 100 -b google >> "$output" 

echo "==========================" 

# SSL/TLS Vulnerability Scanning using SSLyze 
echo "SSL/TLS Vulnerability Scanning using SSLyze" >> "$output" 
sslyze --regular "$target" >> "$output" 

echo "==========================" 

# DNS Enumeration using DNSenum 
echo "DNS Enumeration using DNSenum" >> "$output" 
dnsenum "$target" >> "$output" 

echo "==========================" 

# Web Application Scanning using Wapiti 
echo "Web Application Scanning using Wapiti" >> "$output" 
wapiti "$target" >> "$output" 

echo "==========================" 

# Vulnerability Scanning using OpenVAS 
echo "Vulnerability Scanning using OpenVAS" >> "$output" 
openvas "$target" >> "$output" 

echo "===========END=============" 

echo "Scan completed. Results saved in $output"