import yaml

with open ("test.yaml","w") as f:
    f.dump_data({'a':123,'b':345}, default_style='""')
