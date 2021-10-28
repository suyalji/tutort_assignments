REPO_PATH = "/Users/c58365a/Desktop/tutort/tutort_assignments/WarmUp/"
data = []
with open ('assignment_mukesh_oct_28.txt','a') as fp:
    for i in range(10):
        i += 1
        print(i)
        file = f"Q{i}.py"
        print(f"file: {file}")
        file_name = REPO_PATH+file
        with open(file_name) as q1:
            data = q1.read()
            fp.write("\n")
            fp.write(data)

#with open ('assignment_mukesh_oct_28.txt','a') as fp:
#    fp.write(data)