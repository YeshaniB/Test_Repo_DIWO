# RefactorIQ Python All-Smells Test Repository

Purpose: a deliberately smelly Python project for exercising the CUQA → RDP workflow.

## CUQA smells intentionally included

| CUQA smell | File | Trigger idea | RDP mapping in supplied catalog |
|---|---|---|---|
| LongMethod | `smells/long_method.py` | Function body >30 lines | Extract Method; Replace Temp with Query |
| TooManyParameters | `smells/too_many_parameters.py` | >5 parameters | Introduce Parameter Object; Replace Parameter with Method Call |
| LargeClass | `smells/large_class.py` | >15 methods | Extract Class; Extract Subclass |
| MagicNumber | `smells/magic_number.py` | Suspicious numeric literals | Introduce Constant |
| BareExcept | `smells/bare_except.py` | `except:` | Remove Dead Code; Extract Method |
| DeadCode | `smells/dead_code.py` | Unreferenced function/class | No explicit mapping in supplied RDP catalog |
| DuplicateCode | `smells/duplicate_code.py` | Structurally identical function bodies | No explicit mapping in supplied RDP catalog |
| FeatureEnvy | `smells/feature_envy.py` | Method heavily accesses another object's fields | No explicit mapping in supplied RDP catalog |
| DataClumps | `smells/data_clumps.py` | Same 3+ parameter group repeated | No explicit mapping in supplied RDP catalog |
| SwitchStatements | `smells/switch_statements.py` | 4+ `elif` branches | No explicit mapping in supplied RDP catalog |
| MessageChains | `smells/message_chains.py` | Chained access depth >=3 | No explicit mapping in supplied RDP catalog |
| LazyClass | `smells/lazy_class.py` | <=2 methods and <30 lines | No explicit mapping in supplied RDP catalog |
| PrimitiveObsession | `smells/primitive_obsession.py` | 4+ primitive-typed fields | No explicit mapping in supplied RDP catalog |
| InappropriateIntimacy | `smells/inappropriate_intimacy.py` | Access to another object's `_private` field | No explicit mapping in supplied RDP catalog |
| SpeculativeGenerality | `smells/speculative_generality.py` | ABC/mixin/base-style abstraction | No explicit mapping in supplied RDP catalog |
| Comments | `smells/comments_heavy.py` | >50 LOC and >30% comments | No explicit mapping in supplied RDP catalog |

Run:
```bash
python main.py
```

The code is intentionally bad for analysis purposes. Do not use it as a production coding example.
