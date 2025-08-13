<!-- Slide 1: 📖 MongoDB Indexing Field Guide -->
- **Opening Hook:** "How many of you have seen a query that takes 30 seconds in production but runs instantly on your laptop? Today we're going to fix that forever."

- **Introduction:** "I'm going to teach you to think like MongoDB's query optimizer. By the end of this session, you'll know exactly why your queries are slow and how to make them fast."

---


<!-- Slide 2: 👋 About This Session -->
- **Audience Check:** "Who here has used MongoDB in production? Who has built indexes? Who has cursed at a slow aggregation pipeline? Perfect - you're in the right place."

- **Promise:** "We're going beyond 'just add an index' - you'll understand WHY indexes work, WHEN they don't help, and HOW to design them for your specific use cases."

---


<!-- Slide 3: Single Field Indexes -->
- **Fundamental Truth:** "Single field indexes are your bread and butter. Master these first before getting fancy with compound indexes."

- **Common Mistake:** Developers often skip single field indexes and jump to compound ones too early.

---


<!-- Slide 4: Query Optimizer Overview -->
- **Key Point:** "The optimizer is like a GPS for your data. It has multiple routes but always tries to pick the fastest one. Our job is to build the highways (indexes) it needs."

- **Technical Emphasis:** Stress that the optimizer is cost-based - it's doing math, not magic.

---


<!-- Slide 5: 🔍 Query Optimizer: Stage 1 - Parsing -->
- **Key Insight:** "The optimizer isn't magic - it's methodical. It breaks down your query into parts it can understand and optimize."

- **Walk Through:** "Notice how it categorizes each field by usage: equality matches are the most selective, ranges come next, and sorts determine result order. This categorization drives index selection."

---


<!-- Slide 6: 🔍 Query Optimizer: Stage 1 - Parsing (Field Usage Types) -->
- **Critical Limitation:** "Here's where most developers get stuck - MongoDB can only use one range operation efficiently per query. Multiple ranges = performance problems."

- **Practical Advice:** "When you see queries with $in and $gte together, that's a red flag. Consider restructuring your query or creating multiple optimized indexes."

---


<!-- Slide 7: ⚡ Query Optimizer: Stage 2 - Plan Selection -->
- **Key Point:** [Add speaker notes for this slide]

- **Emphasis:** [Add key talking points]

---


<!-- Slide 8: ESR Rule -->
- **Golden Rule:** "ESR is the most important acronym in MongoDB. If you remember nothing else, remember ESR."

- **Teaching Story:** "A developer once asked me why their compound index wasn't working. They had Range, Sort, Equality. I said 'You're driving backwards on the highway.'"

---


<!-- Slide 9: ESR Rule Deep Dive -->
- **Technical Emphasis:** "MongoDB can only use one range efficiently per query. If you have multiple ranges, only the first one in the index gets optimized."

- **Practical Example:** Relate to filtering a phone book - equality finds the section, sort organizes within it, range picks the subset.

---


<!-- Slide 10: Compound Indexes Introduction -->
- **Key Teaching Moment:** "Compound indexes are like postal addresses. Order matters! '123 Main St, NYC' works. 'NYC, 123 Main St' doesn't make sense."

- **Set Expectations:** "This is where 80% of performance problems get solved or created."

---


<!-- Slide 11: Index Intersection -->
- **Advanced Concept:** "MongoDB can sometimes combine multiple indexes. It's clever, but don't rely on it for performance-critical queries."

- **Best Practice:** "When you need intersection regularly, create a proper compound index instead."

---


<!-- Slide 12: Aggregation Performance Fundamentals -->
- **Transition:** "Now we're moving from simple queries to complex data processing. The rules get more nuanced."

- **Framework:** "Think of aggregation stages like an assembly line. Each stage should make the next one's job easier."

---


<!-- Slide 13: $match Optimization -->
- **Critical Point:** "$match is your performance foundation. Get this wrong and everything downstream suffers."

- **Mantra:** "Filter early, filter often, filter with indexes."

---


<!-- Slide 14: 📈 Aggregation: $match and $sort Optimization (Part 1) -->
- **Optimization Mantra:** "The golden rule: filter early, sort smartly. This slide shows the difference between queries that finish in milliseconds vs ones that timeout."

- **Performance Reality:** "Notice how moving $match before $sort reduces the dataset size. It's like decluttering your desk before organizing it - much easier to sort 100 items than 1 million."

---


<!-- Slide 15: Query Shape Optimization (Part 3) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 16: $lookup Performance -->
- **Major Gotcha:** "$lookup is powerful but dangerous at scale. I call it the 'performance cliff' - works great until it doesn't."

- **Scale Reality:** "What works with 1000 documents fails spectacularly with 1 million."

---


<!-- Slide 17: $lookup Performance Warning -->
- **Dramatic Pause:** "This slide has saved companies from multi-hour queries and potential downtime."

- **Technical Reality:** "MongoDB isn't SQL. $lookup doesn't work like JOINs. Plan accordingly."

---


<!-- Slide 18: $lookup Performance Warning (Part 2) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 19: $lookup Performance Warning (Part 3) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 20: When $lookup Works Well -->
- **Teaching Point:** "Not all $lookup operations are evil. When used correctly with small, filtered datasets, they're perfectly fine."

- **Key Strategy:** "The secret is reducing dataset size BEFORE the lookup, not after."

---


<!-- Slide 21: $lookup Alternatives at Scale -->
- **Design Philosophy:** "Sometimes the best way to optimize a $lookup is to avoid it entirely."

- **Real-World Advice:** "Denormalization isn't a dirty word - it's a valid design choice for performance-critical paths."

---


<!-- Slide 22: $lookup Anti-Pattern Detail -->
- **Production Horror Story:** "I once saw a $lookup bring down a 20-node cluster. The query looked innocent in development."

- **Scale Mathematics:** "Small collections scale linearly. Large collections scale exponentially. Know the difference."

---


<!-- Slide 23: Update/Delete Performance -->
- **Often Overlooked:** "Developers obsess over read performance but forget that writes need indexes too."

- **Practical Impact:** "Slow updates can lock your database and create cascading failures."

---


<!-- Slide 24: Delete Performance -->
- **Scaling Reality:** "Deletes can be trickier than selects. The documents have to be found before they can be removed."

- **Optimization Strategy:** "If you're deleting lots of data regularly, consider TTL indexes or archival strategies."

---


<!-- Slide 25: Mongoose Performance Patterns -->
- **Practical Tips:** "These patterns separate junior developers from senior ones. Small changes, huge impact."

- **Real Impact:** ".lean() alone can make your API 3x faster by skipping Mongoose overhead."

---


<!-- Slide 26: 🔧 Mongoose-Specific Indexing -->
- **Developer Experience:** "Mongoose makes indexes feel like first-class citizens in your code. Your schema becomes your performance documentation."

- **Best Practice:** "Define indexes at the schema level so every developer gets consistent performance. It's like having performance guardrails built into your codebase."

---


<!-- Slide 27: Mongoose Index Definition -->
- **Developer Experience:** "Mongoose makes indexing declarative. Your schema becomes your performance documentation."

- **Team Coordination:** "Schema-level indexes ensure every developer on your team gets the same performance characteristics."

---


<!-- Slide 28: Common Anti-Patterns -->
- **War Stories:** "Every one of these anti-patterns represents a production incident I've seen. Learn from others' pain."

- **Pattern Recognition:** "Good developers recognize these patterns during code review, not in production monitoring."

---


<!-- Slide 29: Too Many Indexes -->
- **Balance Act:** "Indexes are like seasoning. Too little and your queries are bland. Too much and you overwhelm the system."

- **Maintenance Reality:** "Every index you add makes writes slower. Choose wisely."

---


<!-- Slide 30: Cost-Based Decisions (Part 3) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 31: Regex Anti-Patterns -->
- **Critical Point:** "This is one of MongoDB's most misunderstood features. Developers assume all regex queries are the same, but there's a huge performance difference."

- **Teaching Moment:** "Static text like /gmail/ is different from operators like /gm.*il/ - MongoDB can sometimes optimize static patterns."

---


<!-- Slide 32: 🚫 Negative Query Anti-Patterns -->
- **Key Point:** [Add speaker notes for this slide]

- **Emphasis:** [Add key talking points]

---


<!-- Slide 33: 🚫 $lookup Scale Anti-Patterns -->
- **Scale Reality Check:** "This is where developers get burned. $lookup works beautifully in development with 1000 docs, then becomes a disaster in production with 1 million."

- **Prevention Strategy:** "Always ask: 'What happens when this collection has 500K documents?' If the answer scares you, redesign before deployment."

---


<!-- Slide 34: Critical Index Anti-Patterns -->
- **System Impact:** "These aren't just slow queries - they're cluster killers."

- **Recognition Training:** "Practice spotting these patterns during development, not monitoring alerts."

---


<!-- Slide 35: Large $in Arrays -->
- **Practical Limits:** "I've seen developers put 10,000 IDs in a $in query. It doesn't end well."

- **Alternative Strategies:** "Sometimes a lookup table or denormalization is better than a massive $in."

---


<!-- Slide 36: 💥 $in Array Size Anti-Patterns -->
- **Performance Disaster:** "I've seen developers put 10,000 IDs in a $in query and wonder why their app crashes. Size matters!"

- **Real Numbers:** "Watch the performance cliff: 100 IDs = fine, 1,000 IDs = concerning, 10,000 IDs = system killer."

---


<!-- Slide 37: Regex Anti-Patterns (Part 3) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 38: Multikey Index Pitfalls -->
- **Hidden Complexity:** "Arrays seem simple but create complex indexing challenges."

- **Performance Cliff:** "Arrays with hundreds of elements can make indexes unusable."

---


<!-- Slide 39: 🗂️ Array Index Scalability Pitfalls -->
- **Hidden Complexity:** "Arrays look innocent but they're index killers. One document with 500 tags creates 500 index entries!"

- **Memory Explosion:** "I've seen apps crash because a single document had 10,000 array elements. That's 10,000 index entries per document."

---


<!-- Slide 40: Group & Sort Anti-Patterns -->
- **Pipeline Wisdom:** "Order matters in aggregation pipelines. Sort before group when possible."

- **Memory Reality:** "In-memory sorts are performance killers at scale."

---


<!-- Slide 41: Regex Anti-Patterns (Part 2) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 42: 🎯 Compound Index vs Multiple Ranges -->
- **Critical Limitation:** "This is MongoDB's achilles heel - only one range per index scan. Multiple ranges = performance problems."

- **Design Implication:** "When you see queries with multiple $gte, $lte, or $in operations, that's your cue to redesign the query or data model."

---


<!-- Slide 43: Regex Optimization Deep Dive -->
- **Subtle Distinction:** "This is one of MongoDB's best-kept secrets. Not all regex patterns are created equal."

- **Performance Surprise:** "A simple text search can sometimes use indexes even when you don't expect it."

---


<!-- Slide 44: ⚡ MongoDB's Smart Regex Optimizations -->
- **Hidden Intelligence:** "MongoDB is smarter than you think with regex. Static text patterns can sometimes use indexes even when unanchored."

- **Performance Secret:** "The difference between /foo/ and /fo+/ isn't just syntax - it's the difference between index optimization and collection scans."

---


<!-- Slide 45: Regex Performance Reality -->
- **Benchmarking Story:** "These numbers come from real production systems. The differences are dramatic."

- **Design Decision:** "Choose your search strategy based on these performance characteristics."

---


<!-- Slide 46: Single Field Best Practices -->
- **War Story:** "I've seen developers create compound indexes for single-field queries. It works, but it's like using a Ferrari to go to the grocery store - wasteful and unnecessary."

- **Memory Trick:** "Think of cardinality like lanes on a highway. High cardinality = more lanes = less traffic jams."

---


<!-- Slide 47: Regex Best Practices -->
- **Implementation Guide:** "Text indexes vs regex optimization - know when to use which."

- **Performance Planning:** "Case sensitivity isn't just about user experience - it's about performance."

---


<!-- Slide 48: Performance Monitoring -->
- **Operational Excellence:** "You can't optimize what you can't measure."

- **Proactive Approach:** "Set up monitoring before you have problems, not after."


<!-- Slide 49: 🛠️ Index Monitoring & Analysis -->
- **Diagnostic Power:** "explain() is your X-ray vision into MongoDB's decision-making process. Use it religiously."

- **Key Metrics:** "Focus on the ratio: docsExamined vs docsReturned. If you're examining 10,000 to return 10, you have a problem."

---


<!-- Slide 50: 📈 Collection Scan Detection -->
- **Warning Signs:** "COLLSCAN is the four-letter word of MongoDB. When you see it, everything else stops until it's fixed."

- **Emergency Response:** "Collection scans in production are like fire alarms - immediate attention required."

---


<!-- Slide 51: Query Shape Optimization (Part 2) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 52: 🎯 Best Practices Summary -->
- **Actionable Wisdom:** "These aren't theoretical principles - they're battle-tested rules that have saved countless production systems."

- **Implementation Strategy:** "Don't try to implement everything at once. Pick the three most impactful practices for your current codebase and start there."

---


<!-- Slide 53: 🔧 Development Workflow -->
- **Development Integration:** "Indexing isn't a post-deployment afterthought. Build it into your development workflow from day one."

- **Production Readiness:** "Set up profiling in development so you catch performance issues before your users do."

---


<!-- Slide 54: 📚 Tools & Resources -->
- **Tool Mastery:** "MongoDB Compass isn't just pretty - it's powerful. Learn to use these tools before you need them in a crisis."

- **Continuous Learning:** "The MongoDB ecosystem evolves rapidly. Bookmark these resources and check back regularly for new optimization opportunities."

---


<!-- Slide 55: 🚀 Real-World Example -->
- **Practical Application:** "This e-commerce example shows ESR in action. Notice how category and inStock come before price range - that's ESR working."

- **Real Performance Impact:** "This single index design could be the difference between 50ms response times and 5-second timeouts in production."

---


<!-- Slide 56: Cost-Based Decisions (Part 2) -->
- **Continuation:** This slide continues the content from the previous slide.

- **Key Focus:** Maintain the same energy and emphasis from the previous section.

---

<!-- Slide 57: 📋 Action Items -->
- **Immediate Action:** "Don't let this knowledge sit idle. Schedule index audits and profiling setup this week."

- **Prioritization:** "Start with your slowest queries and most critical features. Big impact, manageable scope."

---


<!-- Slide 58: 🎉 Key Takeaways -->
- **Memory Anchors:** "ESR, selectivity, and anti-pattern avoidance - these three concepts will solve 90% of your indexing problems."

- **Mindset Shift:** "Think like the optimizer. Design indexes for how MongoDB searches, not how humans organize data."

---


<!-- Slide 59: 🎉 Key Takeaways -->
- **Performance Culture:** "Make explain() as routine as console.log(). Performance optimization should be part of your daily development."

- **Continuous Improvement:** "Indexing isn't a one-time fix - it's an ongoing optimization practice as your application evolves."

---


<!-- Slide 60: ❓ Questions & Discussion -->
- **Engagement Focus:** "Share your specific challenges - indexing problems are often more nuanced than they first appear."

- **Community Learning:** "The best solutions often come from collective experience. Don't hesitate to describe your use case."

---


<!-- Slide 61: 📖 Additional Resources -->
- **Continuous Learning:** "MongoDB's capabilities evolve rapidly. These resources will help you stay current with new optimization opportunities."

- **Action Planning:** "Don't just bookmark these - set calendar reminders to actually use and explore them."

---

