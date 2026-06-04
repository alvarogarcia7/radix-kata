# 2026-06-04 T 23:24

## Wrong assert 
- [x] There is a wrong assert (marked with a todo). Solve that.

it is inserting:

[F] a
    [F] bc
        [F] d

when it should be 

[F] a
    [F] bc
    [F] d

## Implement pprint better

- [x] show the depth (as in my example above) when printing the tree

# 2026-06-05 T 03:52

- [ ] Implement the self.permute_insert(["a", "b"]) present in the tests. The commented ones are failing
- [ ] reduce duplication between Radix.insert and Node.insert
- [ ] investigate how to have a root that is empty
- [ ] implement hypothesis testing: property-based testing
