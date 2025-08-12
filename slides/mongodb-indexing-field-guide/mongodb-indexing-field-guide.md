---
title: "MongoDB Indexing Field Guide"
subtitle: "Performance & Query Optimization for Node.js Developers"
author: "Database Performance & Query Optimization"
date: "2024"
---

# 📖 MongoDB Indexing Field Guide
## Performance & Query Optimization for Node.js Developers

*Understanding how indexes work and how the optimizer evaluates your queries*

---
# 👋 About This Session

**Target Audience:** Node.js & Mongoose developers (all levels)

**What You'll Learn:**
- How MongoDB's query optimizer really works
- Index types and when to use them
- Query patterns that help/hurt performance
- Aggregation pipeline optimization
- Mongoose-specific indexing considerations
- Common pitfalls and how to avoid them

---
# 🎯 Why Indexes Matter

    // Without index: O(n) - scans entire collection
    db.users.find({ email: "john@example.com" })

    // With index: O(log n) - direct lookup
    db.users.createIndex({ email: 1 })
    db.users.find({ email: "john@example.com" })

**Performance Impact:**
- 1M documents: ~1ms vs ~1000ms
- 10M documents: ~1ms vs ~10,000ms
- Linear growth vs logarithmic growth

---
# 🧠 MongoDB Query Optimizer Overview

## The Three-Stage Process

1. **Query Parsing** - Understands what you want
2. **Plan Selection** - Chooses how to get it
3. **Execution** - Actually runs the query

The optimizer is **cost-based** and **learned** - it remembers what works!

---
# 🔍 Query Optimizer: Stage 1 - Parsing

    // Your query
    db.users.find({ 
      status: "active", 
      age: { $gte: 25 }, 
      city: "New York" 
    }).sort({ lastLogin: -1 })

    // Optimizer identifies:
    // - Filter fields: status, age, city
    // - Filter types: equality, range, equality  
    // - Sort fields: lastLogin (descending)
    // - Operation type: find

---
# 🔍 Query Optimizer: Stage 1 - Parsing (Field Usage Types)

**Field Usage Types:**
- **Equality**: `status: "active"`
- **Range**: `age: { $gte: 25 }`
- **Sort**: `sort({ lastLogin: -1 })`

---
# ⚡ Query Optimizer: Stage 2 - Plan Selection

## Index Candidate Evaluation

    // Available indexes:
    { status: 1 }                    // Single field
    { age: 1, status: 1 }           // Compound
    { city: 1, lastLogin: -1 }      // Compound with sort
    { status: 1, lastLogin: -1 }    // ESR pattern

**Optimizer considers:**
- **Field coverage** - Which fields can use index
- **Selectivity** - How much data gets filtered out
- **Sort efficiency** - Can index provide sort order

---
# 🎯 The ESR Rule (Equality, Sort, Range)

## Optimal Index Field Order

    // Query pattern
    db.users.find({ 
      status: "active",        // Equality
      age: { $gte: 25 }       // Range
    }).sort({ lastLogin: -1 }) // Sort

    // Optimal index: ESR order
    { status: 1, lastLogin: -1, age: 1 }
    //   E          S            R

**Why ESR works:**
1. **Equality** - Most selective, finds exact matches
2. **Sort** - Provides sorted results without extra work
3. **Range** - Filters remaining documents

---
# 📊 Index Types Deep Dive

## Single Field Indexes

    // Basic single field
    db.users.createIndex({ email: 1 })

    // Good for:
    db.users.find({ email: "john@example.com" })
    db.users.find({ email: { $in: ["john@example.com", "jane@example.com"] } })

    // Direction matters for sorting:
    db.users.createIndex({ createdAt: -1 })  // Newest first

---
# 🔗 Compound Indexes

    // Order matters!
    db.users.createIndex({ status: 1, age: 1, city: 1 })

    // Can efficiently support:
    { status: "active" }
    { status: "active", age: 25 }
    { status: "active", age: 25, city: "NYC" }

    // Cannot efficiently support:
    { age: 25 }                    // Skips first field
    { city: "NYC" }               // Skips first fields
    { age: 25, city: "NYC" }      // Skips first field

**Left-to-Right Rule:** Must use fields from left to right

---
# 🎨 Specialized Index Types

## Text Indexes
    db.articles.createIndex({ title: "text", content: "text" })
    db.articles.find({ $text: { $search: "mongodb indexing" } })

## Geospatial Indexes
    db.places.createIndex({ location: "2dsphere" })
    db.places.find({ location: { $near: { $geometry: { type: "Point", coordinates: [-73.97, 40.77] } } } })

## Partial Indexes
    db.users.createIndex({ email: 1 }, { partialFilterExpression: { status: "active" } })

---
# 🔄 Aggregation Pipeline Optimization

## Pipeline Stages and Indexes

    db.users.aggregate([
      { $match: { status: "active", age: { $gte: 25 } } },  // Can use index
      { $sort: { lastLogin: -1 } },                         // Can use index
      { $group: { _id: "$department", count: { $sum: 1 } } }, // Creates new data
      { $sort: { count: -1 } }                              // Needs in-memory sort
    ])

    // Optimal index:
    { status: 1, lastLogin: -1, age: 1 }

**Key Principle:** Early pipeline stages can use indexes, later stages often can't

---
# 📈 Aggregation: $match and $sort Optimization

    // GOOD: $match first, then $sort
    db.orders.aggregate([
      { $match: { status: "completed", date: { $gte: new Date("2024-01-01") } } },
      { $sort: { amount: -1 } },
      { $limit: 10 }
    ])

    // Index: { status: 1, amount: -1, date: 1 }

---
# 📈 Aggregation: $match and $sort Optimization (Part 1)

    // BAD: $sort before selective $match
    db.orders.aggregate([
      { $sort: { amount: -1 } },  // Sorts entire collection!
      { $match: { status: "completed" } },
      { $limit: 10 }
    ])

---
# 📈 Aggregation: $match and $sort Optimization (Part 3)

---
# 🎯 Aggregation: $lookup Optimization

    // Users collection
    db.users.createIndex({ _id: 1 })              // Default
    db.users.createIndex({ department: 1 })       // For lookup

    // Orders collection  
    db.orders.createIndex({ userId: 1 })           // For lookup

    db.orders.aggregate([
      { $match: { status: "pending" } },           // Use index on orders
      { $lookup: {
          from: "users",
          localField: "userId",                     // Uses userId index
          foreignField: "_id",                      // Uses _id index
          as: "user"
      }}
    ])

---
# ⚠️ $lookup Performance Pitfalls

## The Hidden Scalability Problem

    // LOOKS GOOD in development (1K docs)
    db.orders.aggregate([
      { $lookup: {
          from: "products",
          localField: "productId",
          foreignField: "sku",              // NOT _id!
          as: "product"
      }}
    ])

    // DISASTER in production (500K+ docs)
    // Each lookup becomes individual query!
    // 10,000 orders = 10,000 separate index lookups

**Reality Check:** $lookup doesn't work like SQL JOINs

---
# 🚨 $lookup: When It Goes Wrong

## Problem Scenarios

    // BAD: Non-_id field lookups at scale
    { $lookup: { foreignField: "email" } }        // Slow with large collections
    { $lookup: { foreignField: "customerId" } }   // Not optimized like _id

    // BAD: Complex filtering in lookup
    { $lookup: {
        from: "users",
        let: { orderId: "$_id" },
        pipeline: [
          { $match: { 
              $expr: { $eq: ["$orders", "$$orderId"] },
              status: "active",                      // Additional filtering
              region: { $in: ["US", "CA"] }         // Compound conditions
          }}
        ]
    }}

---
# 🚨 $lookup: When It Goes Wrong (Performance)

**Performance Impact:** O(n × m) instead of expected O(log n)

---
# 📊 $lookup Performance Reality

## The Numbers Don't Lie

    // Small scale (1-10K docs): Works fine
    Orders: 5,000 documents
    Users: 2,000 documents  
    Lookup time: ~50ms ✅

    // Medium scale (50-100K docs): Starts degrading
    Orders: 75,000 documents
    Users: 50,000 documents
    Lookup time: ~2,500ms ⚠️

    // Large scale (500K+ docs): Major performance issues
    Orders: 500,000 documents  
    Users: 200,000 documents
    Lookup time: ~45,000ms ❌ (45 seconds!)

---
# ✅ When $lookup Works Well

## Efficient $lookup Patterns

    // GOOD: _id lookups (always fast)
    { $lookup: { foreignField: "_id" } }

    // GOOD: Small, filtered datasets first
    db.orders.aggregate([
      { $match: { date: { $gte: today } } },      // Reduce dataset FIRST
      { $limit: 100 },                            // Limit early
      { $lookup: { ... } }                        // Then lookup
    ])

**Key Strategy:** Filter and limit before lookup operations

---
# 🔄 $lookup Alternatives at Scale

## Better Patterns for Large Collections

    // Option 1: Embed data (denormalization)
    {
      _id: ObjectId("..."),
      productName: "iPhone 14",                   // Embed frequently accessed data
      productPrice: 999,
      productSku: "IPHONE14-128"
    }

    // Option 2: Application-level joins
    const orders = await db.orders.find({ status: "pending" });
    const userIds = orders.map(o => o.userId);
    const users = await db.users.find({ _id: { $in: userIds } });

**Performance Tip:** Sometimes avoiding $lookup entirely is the best solution

---
# ✏️ Update & Delete Optimization

## Update Operations

    // Single document update - uses index
    db.users.updateOne(
      { email: "john@example.com" },      // Filter uses index
      { $set: { lastLogin: new Date() } }
    )

    // Multi-document update - benefits from index
    db.users.updateMany(
      { status: "inactive" },             // Filter uses index
      { $set: { archived: true } }
    )

    // Index needed: { email: 1 } and { status: 1 }

---
# 🗑️ Delete Optimization

    // Efficient delete with index
    db.users.deleteMany({ 
      status: "inactive", 
      lastLogin: { $lt: new Date("2023-01-01") } 
    })

    // Optimal index: { status: 1, lastLogin: 1 }

**Key Point:** Delete operations scan first, then delete. Good indexes make the scan fast!

---
# 🔧 Mongoose-Specific Indexing

## Schema-Level Index Definition

    const userSchema = new mongoose.Schema({
      email: { 
        type: String, 
        required: true,
        index: true,        // Single field index
        unique: true        // Unique constraint
      },
      status: String,
      age: Number,
      lastLogin: Date
    });

    // Compound indexes
    userSchema.index({ status: 1, age: 1 });
    userSchema.index({ status: 1, lastLogin: -1 });

---
# 🔧 Mongoose-Specific Indexing (Part 2)

---
# 🚀 Mongoose Query Optimization

    // GOOD: Use lean() for read-only queries
    const users = await User.find({ status: "active" })
      .lean()                    // Skip Mongoose document wrapper
      .select('name email')      // Project only needed fields
      .limit(100);

    // GOOD: Use explain() to check query plans
    const explained = await User.find({ status: "active" }).explain();
    console.log(explained.executionStats);

    // GOOD: Use proper field types
    const User = new Schema({
      _id: { type: mongoose.Schema.Types.ObjectId }, // Proper ObjectId
      email: { type: String, lowercase: true }        // Consistent format
    });

---
# ⚠️ Common Pitfalls & Anti-Patterns

## 1. Wrong Index Field Order

    // BAD: Wrong order for this query
    db.users.createIndex({ age: 1, status: 1 })
    db.users.find({ status: "active", age: { $gte: 25 } }).sort({ name: 1 })

    // GOOD: Follow ESR principle
    db.users.createIndex({ status: 1, name: 1, age: 1 })

---
# ⚠️ Common Pitfalls & Anti-Patterns (2. Too Many Indexes)

## 2. Too Many Indexes

    // BAD: Index overload
    db.users.createIndex({ email: 1 })
    db.users.createIndex({ status: 1 })
    db.users.createIndex({ age: 1 })
    db.users.createIndex({ city: 1 })
    // Every write now updates 5 indexes!

---
# ⚠️ Common Pitfalls & Anti-Patterns (Part 3)

---
# 🚫 Regex Anti-Patterns

## Regex Optimization Misunderstandings

    // BAD: Unanchored with regex operators
    db.users.find({ email: { $regex: /gm.*il/ } })      // Collection scan!

    // OK: Static text (MongoDB can sometimes optimize)
    db.users.find({ email: { $regex: /gmail/ } })       // May use index bounds

    // GOOD: Left-anchored regex can use index
    db.users.find({ email: { $regex: /^john/ } })

**Key Point:** Regex operators (`.`, `*`, `+`) prevent index usage when unanchored

**See regex optimization deep dive for complete details**

---
# 🚫 Negative Query Anti-Patterns

## $ne and $nin Performance Problems

    // BAD: These scan entire collection
    db.users.find({ status: { $ne: "deleted" } })
    db.users.find({ status: { $nin: ["deleted", "banned"] } })

    // GOOD: Use positive conditions instead
    db.users.find({ status: { $in: ["active", "pending"] } })

**Why This Matters:** Negative queries examine most documents in your collection

---
# 🚫 $lookup Scale Anti-Patterns

## Naive $lookup Assumptions

    // BAD: Assumes $lookup scales like SQL JOINs
    db.orders.aggregate([
      { $lookup: { foreignField: "customerId" } }  // Disaster with 500K+ docs!
    ])

    // GOOD: Filter first, lookup small datasets
    db.orders.aggregate([
      { $match: { date: { $gte: today } } },      // Reduce dataset FIRST
      { $lookup: { foreignField: "customerId" } }
    ])

**Reality Check:** $lookup doesn't work like SQL JOINs at scale

---
# 🚨 Critical Index Anti-Patterns

## Multiple Range Queries = Index Disaster

    // BAD: Multiple ranges can't use compound index efficiently
    db.products.find({ 
      price: { $gte: 100, $lte: 500 },      // Range 1
      weight: { $gte: 1, $lte: 10 },        // Range 2  
      rating: { $gte: 4.0 }                 // Range 3
    })

    // Index: { price: 1, weight: 1, rating: 1 }
    // Reality: Only price range can use index efficiently!
    // weight and rating become collection scans

**Rule:** Only ONE range condition per query can use index efficiently

---
# 💥 $in Array Size Anti-Patterns

## When $in Becomes Your Enemy

    // BAD: Large $in arrays kill performance
    const userIds = [...Array(10000)].map(() => new ObjectId()); // 10K IDs!
    db.orders.find({ userId: { $in: userIds } })

    // Performance characteristics:
    // 100 IDs in $in: ~50ms ✅
    // 1,000 IDs in $in: ~500ms ⚠️  
    // 10,000 IDs in $in: ~15,000ms ❌ (15 seconds!)

---
# 💥 $in Array Size Anti-Patterns (Better Approaches)

**Better Approaches:**
    // Option 1: Batch processing
    for (const batch of chunks(userIds, 500)) {
      await db.orders.find({ userId: { $in: batch } });
    }

    // Option 2: Flip the query
    db.orders.find({ userId: { $exists: true } })
      .forEach(order => {
        if (userIdSet.has(order.userId)) { /* process */ }
      });

---
# 💥 $in Array Size Anti-Patterns (Part 3)

---
# 🗂️ Array Index Scalability Pitfalls

## Multikey Index Performance Degradation

    // Document with large arrays
    {
      _id: ObjectId("..."),
      tags: ["electronics", "mobile", "smartphone", /* ...500 more tags */],
      categories: ["tech", "gadgets", /* ...200 more categories */]
    }

    // Index on array fields
    db.products.createIndex({ tags: 1, categories: 1 })

    // Problems:
    // 1. Index size explodes: 500 × 200 = 100,000 index entries per document!
    // 2. Write performance degrades severely
    // 3. Memory usage skyrockets

---
# 🗂️ Array Index Scalability Pitfalls (Solutions)

**Solutions:**
    // Option 1: Limit array sizes
    { maxArraySize: 50 }  // Enforce in application

    // Option 2: Use text index for searchable arrays
    db.products.createIndex({ tags: "text" })

    // Option 3: Separate collection for array items
    // products collection + product_tags collection

---
# 📊 Group & Sort Anti-Patterns

## The Wrong Order Trap

    // BAD: Sort after group = in-memory sort
    db.orders.aggregate([
      { $group: { 
          _id: "$customerId", 
          totalAmount: { $sum: "$amount" },
          orderCount: { $sum: 1 }
      }},
      { $sort: { totalAmount: -1 } }        // Can't use index!
    ])

    // GOOD: Sort before group when possible
    db.orders.aggregate([
      { $sort: { customerId: 1, amount: -1 } },  // Uses index
      { $group: { 
          _id: "$customerId",
          maxAmount: { $first: "$amount" },       // Pre-sorted!
          totalAmount: { $sum: "$amount" }
      }}
    ])

    // Index: { customerId: 1, amount: -1 }

---
# 📊 Group & Sort Anti-Patterns (Part 2)

---
# 🎯 Compound Index vs Multiple Ranges

## The Selectivity Problem

    // BAD: Low selectivity fields with ranges
    db.events.find({
      type: "click",                         // Low selectivity (90% of docs)
      timestamp: { $gte: yesterday },        // Range
      userId: { $in: [1000 user IDs] }      // High selectivity
    })

    // Index: { type: 1, timestamp: 1, userId: 1 }
    // Problem: Scans 90% of collection before filtering!

    // GOOD: High selectivity first
    // Index: { userId: 1, type: 1, timestamp: 1 }
    // Finds specific users first, then filters

**Selectivity Rule:** Most selective fields first, especially before ranges

---
# 🔍 Regex Optimization Deep Dive

## Static Text vs Regex Operators

    // SURPRISING: These can sometimes use indexes even unanchored!
    db.users.find({ name: { $regex: /john/ } })        // Static text
    db.users.find({ name: { $regex: /smith/ } })       // Static text
    db.users.find({ name: { $regex: /admin/ } })       // Static text

    // NEVER optimized: Regex operators can't use index unanchored
    db.users.find({ name: { $regex: /joh+n/ } })       // + operator
    db.users.find({ name: { $regex: /sm.*th/ } })      // . and * operators  
    db.users.find({ name: { $regex: /admin?/ } })      // ? operator

**Key Insight:** MongoDB can sometimes optimize static text searches

---
# ⚡ MongoDB's Smart Regex Optimizations

## The Hidden Index Magic

    // Index: { name: 1 }

    // MongoDB CAN optimize these (static text):
    /john/           // Looks for "john" substring - can use index bounds!
    /smith/          // Looks for "smith" substring
    /company/        // Static text pattern

    // MongoDB CANNOT optimize these (regex operators):
    /joh+n/          // + means "one or more h" - infinite possibilities
    /sm.*th/         // .* means "anything between" - too broad
    /compan(y|ies)/  // Alternation - multiple patterns

**Performance Impact:**
- Static text: Can narrow index scan range
- Regex operators: Always full collection scan (unless anchored)

---
# 📊 Regex Performance Comparison

## Real Performance Numbers

    // Test collection: 1M user documents with name field indexed

    // Static unanchored (optimizable)
    db.users.find({ name: { $regex: /smith/ } })
    // Index bounds: ["smith", "smithz")  
    // Performance: ~100ms, examines ~1000 docs ✅

    // Regex operator unanchored (not optimizable)  
    db.users.find({ name: { $regex: /smit+h/ } })
    // No index bounds possible
    // Performance: ~5000ms, examines ALL 1M docs ❌

    // Left-anchored (always optimizable)
    db.users.find({ name: { $regex: /^smit+h/ } })
    // Index bounds: ["smit", "smiu")
    // Performance: ~50ms, examines ~100 docs ✅

---
# 🎯 Regex Best Practices

## Optimization Strategy

    // BEST: Use text indexes for complex searches
    db.users.createIndex({ name: "text", email: "text" })
    db.users.find({ $text: { $search: "john smith" } })

    // GOOD: Left-anchor when possible
    db.users.find({ email: { $regex: /^john.*@company\.com$/ } })

    // OK: Static text (MongoDB optimizes some cases)
    db.users.find({ name: { $regex: /john/ } })

    // BAD: Unanchored with regex operators
    db.users.find({ name: { $regex: /joh+n.*smith/ } })

---
# 🎯 Regex Best Practices (Case Sensitivity Gotcha)

## Case Sensitivity Gotcha
    // BAD: Case-insensitive kills optimization
    db.users.find({ name: { $regex: /john/i } })        // Collection scan!

    // GOOD: Store data in consistent case
    db.users.find({ name: { $regex: /john/ } })         // Can optimize
    // Ensure data is stored as: "John Smith" or "john smith" consistently

---
# 📊 Selectivity and Performance

## Understanding Selectivity

    // High selectivity (GOOD) - finds few documents
    db.users.find({ email: "john@example.com" })      // 1 out of 1M

    // Medium selectivity (OK) - finds some documents  
    db.users.find({ city: "New York" })               // 50K out of 1M

    // Low selectivity (BAD) - finds many documents
    db.users.find({ status: "active" })               // 900K out of 1M

**Rule:** More selective fields should come first in compound indexes

---
# 🛠️ Index Monitoring & Analysis

## Using explain()

    // Get execution statistics
    const result = await db.users.find({ status: "active" }).explain("executionStats");

    console.log({
      indexUsed: result.executionStats.executionStages.indexName,
      docsExamined: result.executionStats.totalDocsExamined,
      docsReturned: result.executionStats.totalDocsReturned,
      executionTime: result.executionStats.executionTimeMillis
    });

**Key Metrics:**
- `totalDocsExamined` vs `totalDocsReturned` (lower ratio = better)
- `executionTimeMillis` (lower = better)
- `indexName` (should not be null)

---
# 📈 Collection Scan Detection

    // Signs of collection scans:
    {
      "stage": "COLLSCAN",                    // No index used
      "totalDocsExamined": 1000000,           // Examined all docs
      "totalDocsReturned": 1,                 // Returned few docs
      "executionTimeMillis": 1250             // High execution time
    }

    // Good index usage:
    {
      "stage": "IXSCAN",                      // Index scan
      "indexName": "status_1_age_1",          // Used specific index
      "totalDocsExamined": 5,                 // Examined few docs
      "totalDocsReturned": 5,                 // Returned matched docs
      "executionTimeMillis": 2                // Fast execution
    }

---
# 📈 Collection Scan Detection (Part 2)

---
# 🎯 Best Practices Summary

## Index Design
1. **Follow ESR rule** for compound indexes
2. **Put selective fields first** in compound indexes
3. **Create indexes for your query patterns**, not your data structure
4. **Use covering indexes** when possible
5. **Limit array sizes** to prevent multikey index explosion

## Query Writing
1. **Avoid $ne, $nin, and unanchored regex with operators**
2. **Use projection** to limit returned fields
3. **Limit result sets** with `.limit()`
4. **Use explain()** to verify index usage
5. **Batch large $in arrays** (max ~500-1000 items)
6. **Only one range condition** per query
7. **Sort before group** when possible
8. **Prefer static text regex** over operator-based patterns

---
# 🔧 Development Workflow

## 1. Development Phase
    // Enable profiling for slow queries
    db.setProfilingLevel(2, { slowms: 100 })

    // Use explain in development
    const query = User.find({ status: "active" });
    console.log(await query.explain());

## 2. Production Monitoring
    // Monitor slow operations
    db.runCommand({ profile: 0 })
    db.system.profile.find().sort({ ts: -1 }).limit(5)

    // Check index usage statistics
    db.users.aggregate([{ $indexStats: {} }])

---
# 📚 Tools & Resources

## MongoDB Tools
- **MongoDB Compass** - Visual index analysis
- **db.collection.explain()** - Query plan analysis
- **Database Profiler** - Slow query detection
- **$indexStats** - Index usage statistics

## Mongoose Tools
- **query.explain()** - Mongoose wrapper for explain
- **Schema.index()** - Schema-level index definition
- **mongoose.set('debug', true)** - Query logging

---
# 🚀 Real-World Example

    // E-commerce product search
    const productSchema = new Schema({
      name: String,
      category: String,
      price: Number,
      inStock: Boolean,
      rating: Number,
      tags: [String]
    });

    // Query: Find in-stock products in category, sorted by rating
    Product.find({ 
      category: "electronics",     // Equality
      inStock: true,              // Equality  
      price: { $lte: 1000 }       // Range
    }).sort({ rating: -1 })       // Sort

    // Optimal index: ESR pattern
    productSchema.index({ category: 1, inStock: 1, rating: -1, price: 1 });

---
# 🚀 Real-World Example (Part 2)

---
# 📋 Action Items

## Immediate Steps
1. **Audit existing queries** - Run explain() on slow queries
2. **Review current indexes** - Remove unused, add missing
3. **Enable query profiling** - Identify problematic queries
4. **Add schema-level indexes** - Define in Mongoose schemas

## Ongoing Practices
1. **Test query performance** - Use explain() in development
2. **Monitor production metrics** - Track slow queries and index usage
3. **Regular index maintenance** - Review and optimize quarterly

---
# 🎉 Key Takeaways

## Remember These Rules
1. **Indexes are about query patterns, not data structure**
2. **ESR (Equality, Sort, Range) for compound indexes**
3. **Left-to-right rule for compound index usage**
4. **High selectivity fields come first**
5. **Every index has a write cost**
6. **Only ONE range query can use index efficiently**
7. **Large $in arrays (>1000) kill performance**
8. **Array indexes explode with large/multiple arrays**
9. **Static text regex (/foo/) can optimize, operators (/foo+/) cannot**

---
# 🎉 Key Takeaways (Critical Anti-Patterns to Avoid)

## Critical Anti-Patterns to Avoid
- Multiple range conditions in one query
- $lookup on non-_id fields at scale
- Sort after group operations
- Large multikey indexes
- Unanchored regex with operators (+, *, ?, etc.)

## Test, Monitor, Optimize
- Use `explain()` religiously
- Monitor slow query logs
- Regular performance reviews

---
# ❓ Questions & Discussion

## Let's talk about:
- Your specific query patterns
- Performance challenges you're facing
- Index strategies for your use cases
- Mongoose optimization techniques

**Thank you for attending!**
*Happy indexing! 🚀*

---
# 📖 Additional Resources

## Documentation
- [MongoDB Index Documentation](https://docs.mongodb.com/manual/indexes/)
- [Mongoose Index Documentation](https://mongoosejs.com/docs/guide.html#indexes)
- [Query Optimization Guide](https://docs.mongodb.com/manual/core/query-optimization/)

## Tools
- [MongoDB Compass](https://www.mongodb.com/products/compass)
- [Studio 3T](https://studio3t.com/) - Query profiling
- [IndexAnalyzer](https://github.com/your-repo/IndexAnalyzer) - Automated index analysis
- [MongoDB Indexing Field Guide](https://github.com/your-repo/IndexAnalyzer/tree/main/slides) - This presentation

*Contact: [your-email@company.com]* 