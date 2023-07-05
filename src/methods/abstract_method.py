
class AbstractMethods:
    def __init__(self, prompt, test, entry_point):
        self.prompt = prompt
        self.test = test
        self.entry_point = entry_point

    def combine_desc_testcases(self, lang, func_entry, comments, test_demo):
        if lang == 'py':
            new_prompt = self.combine_desc_testcases_py(func_entry, comments, test_demo)
        else:
            raise NotImplementedError
        return new_prompt

    def combine_desc_testcases_py(self, func_entry, comments, test_demo):
        return func_entry + "\n" + comments + '>>> '.join([""] + test_demo)

    def split_desc_testcases(self, lang):
        if lang == 'py':
            func_entry, comments, test_demo = self.split_desc_testcases_py()
        else:
            raise NotImplementedError
        return func_entry, comments, test_demo

    def split_desc_testcases_py(self):
        prompt = self.prompt
        # find all tests from prompt
        split_prompt = prompt.split('>>> ')
        desc, test_demo = split_prompt[0], split_prompt[1:]
        desc_split = desc.split("\n")
        func_entry, comments = desc_split[0], "\n".join(desc_split[1:])
        return func_entry, comments, test_demo

