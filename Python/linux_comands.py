import subprocess

class LinuxComands:
    def __init__(self):
        pass

    def execute_comad(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            error = result.stderr.decode('utf-8')
            return output, error
        except subprocess.CalledProcessError as e:
            return None, e.stderr

    def list_items(self, path="."):
        comand=f"ls {path}"
        return self.execute_comad(comand)

    def pwd(self):
        command = "pwd"
        return  self.execute_comad(command)

    def move(self, source, destination):
        command=f"mv {source} {destination}"
        return self.execute_comad(command)

    def copy(self, source, destination):
        command=f"cp {source} {destination}"
        return self.execute_comad(command)

    def remove(self, file):
        command=f"rm -r {file}"
        return self.execute_comad(command)

    def create_file(self, filename):
        command=f"touch {filename}"
        return self.execute_comad(command)

if __name__ == '__main__':
    linux_comnds=LinuxComands()

    output, error = linux_comnds.pwd()
    print("pwd:", output , error)


    output, error = linux_comnds.move("~/Downloads/log.txt", "~/PycharmProjects/InternshipProject")
    print("move:", output , error)

    output, error = linux_comnds.copy("~/Downloads/bashcrc.txt", "~/PycharmProjects/InternshipProject")
    print("copy:", output , error)

    output, error = linux_comnds.create_file("new_file.txt")
    print("creat file:", output , error)

    output, error = linux_comnds.list_items()
    print("ls:", output, error)

    output, error = linux_comnds.remove("new_file.txt")
    print("remove:", output , error)

    output, error = linux_comnds.list_items()
    print("ls:", output , error)


