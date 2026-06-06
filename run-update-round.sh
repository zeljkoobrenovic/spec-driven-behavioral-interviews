echo "CLAUDE: Starting update round for $1/interview.json by reviewing the content and improving it based on the review."
claude -p "Review $1/interview.json using the review-behavioral-interview skill." --allowedTools "Read,Write,Edit,Bash"

echo "CODEX: Review of $1/interview.json has been updated. Now improving the content based on the review."
codex exec "Improve $1/interview.json based on REVIEW.md."

echo "CLAUDE: Updating review of $1/interview.json based on recent changes and improving the content based on the review."
claude -p "Update review of $1/interview.json based on recent changes using the review-system-design-interview skill." --allowedTools "Read,Write,Edit,Bash"

echo "CODEX: Improving $1/interview.json based on the updated review."
codex exec "Improve $1/interview.json based on the updated REVIEW.md"

echo "CODEX: Polishing $1/interview.json for better understandability, readability, flows, and overall quality."
codex exec "Make one more pass in $1/interview.json of lightweight edits and polishing to improve understandability, readability, flows, and overall quality."

echo "CODEX: Adding external links to $1/interview.json."
codex exec "Add external links to $1/interview.json using the research-external-links skill."

echo "CODEX: Writing a LinkedIn post for $1/interview.json and storing it into $1/LINKEDIN.md."
codex exec "Write a LinkedIn Post for $1/interview.json and store it into $1/LINKEDIN.md."

echo "NANO BANANA: Generating images."
rm -rf $1/assets
cd _scripts
python3 generate_interview_assets.py ../$1/interview.json

cd ..
python3 build.py
