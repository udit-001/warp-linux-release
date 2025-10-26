#!/usr/bin/env python3
"""
Script to fetch Warp version information from the download endpoint.
Extracts the download URL and version number for GitHub Actions workflow.
"""

import requests
import re
import os
import sys


def main():
    print("Fetching Warp download URL...")
    
    try:
        # Make request and follow redirects
        response = requests.get("https://app.warp.dev/download?package=appimage", allow_redirects=False)
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code != 302:
            print(f"Error: Expected 302 redirect, got {response.status_code}")
            sys.exit(1)
        
        # Get the redirect URL from Location header
        redirect_url = response.headers.get('Location')
        if not redirect_url:
            print("Error: No Location header found in response")
            sys.exit(1)
        
        print(f"Redirect URL: {redirect_url}")
        
        # Extract version from URL path using regex
        # Looking for pattern like: v0.2025.10.22.08.13.stable_02
        print(f"Trying to extract version from: {redirect_url}")
        
        # Let's try multiple patterns to see what works
        patterns = [
            r'v\d+\.\d+\.\d+\.\d+\.\d+\.\w+_\d+',  # v0.2025.10.22.08.13.stable_02
            r'v\d+\.\d+\.\d+\.\d+\.\d+\.\w+\.\d+',  # v0.2025.10.22.08.13.stable.02
            r'v\d+\.\d+\.\d+\.\d+\.\d+\.\w+',       # v0.2025.10.22.08.13.stable
            r'v\d+\.\d+\.\d+\.\d+\.\d+',            # v0.2025.10.22.08.13
        ]
        
        version_match = None
        for i, pattern in enumerate(patterns):
            print(f"Trying pattern {i+1}: {pattern}")
            match = re.search(pattern, redirect_url)
            if match:
                print(f"Pattern {i+1} matched: '{match.group(0)}'")
                version_match = match
                break
            else:
                print(f"Pattern {i+1} did not match")
        
        if not version_match:
            print(f"Error: Could not extract version from URL: {redirect_url}")
            # Let's see what we can find
            all_matches = re.findall(r'v\d+.*?\d+', redirect_url)
            print(f"Found potential versions: {all_matches}")
            # Try to find anything that starts with v
            v_matches = re.findall(r'v[^/]*', redirect_url)
            print(f"Found v-prefixed strings: {v_matches}")
            sys.exit(1)
        
        version = version_match.group(0)
        print(f"Extracted version: {version}")
        
        # Write outputs to GitHub Actions environment
        github_output = os.environ.get('GITHUB_OUTPUT')
        if github_output:
            with open(github_output, 'a') as f:
                f.write(f"x64_download_url={redirect_url}\n")
                f.write(f"x64_version={version}\n")
                f.write(f"version={version}\n")  # Also set as generic version
                f.write(f"download_url={redirect_url}\n")  # Also set as generic download_url
        else:
            # For local testing
            print(f"x64_download_url={redirect_url}")
            print(f"x64_version={version}")
            print(f"version={version}")
            print(f"download_url={redirect_url}")
        
        print("Successfully extracted Warp version info")
        
    except requests.RequestException as e:
        print(f"Error making request: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
