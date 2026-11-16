import time

class OpenSourceProject:
    def __init__(self, name, initial_version="1.0.0"):
        self.name = name
        self.version = initial_version
        self.features = []
        self.bug_fixes = []
        self.contributors = set()
        print(f"[{self.name}] Project initialized at version {self.version}")

    def add_contributor(self, contributor_name):
        self.contributors.add(contributor_name)
        print(f"[{self.name}] {contributor_name} joined the community.")

    def add_feature(self, feature_name, contributor="Community"):
        self.features.append(f"{feature_name} (by {contributor})")
        print(f"[{self.name}] New feature added: '{feature_name}' by {contributor}.")
        # This represents the growth and innovation that sponsorship helps enable.
        # (Article: "yeni özelliklerin geliştirilmesi" - development of new features)

    def fix_bug(self, bug_description, contributor="Community"):
        self.bug_fixes.append(f"{bug_description} (by {contributor})")
        print(f"[{self.name}] Bug fixed: '{bug_description}' by {contributor}.")
        # This represents crucial maintenance and security, often supported by funding.
        # (Article: "güvenlik açıklarının hızla giderilmesi" - rapid fixing of security vulnerabilities)

    def release_new_version(self):
        major, minor, patch = map(int, self.version.split('.'))
        patch += 1
        new_version = f"{major}.{minor}.{patch}"
        self.version = new_version
        print(f"\n[{self.name}] Releasing new version {self.version}!")
        print(f"  - Total Features: {len(self.features)}")
        for feature in self.features:
            print(f"    * {feature}")
        print(f"  - Total Bug Fixes: {len(self.bug_fixes)}")
        for bug in self.bug_fixes:
            print(f"    * {bug}")
        print(f"  - Active Contributors: {len(self.contributors)}")
        print(f"  This release demonstrates the project's sustainability and growth.")
        # The ability to consistently release new versions shows project health,
        # often a direct result of sustained contributions (volunteer or sponsored).
        # (Article: "projelerin sürdürülebilirliği" - sustainability of projects)

# --- Main simulation --- 
if __name__ == "__main__":
    my_os_project = OpenSourceProject("MyOSLib")

    print("\n--- Initial Development Phase (Community Driven) ---")
    my_os_project.add_contributor("Alice (Volunteer)")
    my_os_project.add_feature("Basic data serialization", "Alice (Volunteer)")
    my_os_project.fix_bug("Minor typo in documentation", "Bob (Volunteer)")
    time.sleep(0.5)

    my_os_project.release_new_version()

    print("\n--- Post-Sponsorship Phase (Accelerated Development) ---")
    # Simulate the impact of increased resources, e.g., through sponsorship.
    # This allows for more focused and professional development.
    # (Article: "daha profesyonel bir şekilde yönetilmesi" - managed more professionally)
    my_os_project.add_contributor("Charlie (Sponsored Dev)")
    my_os_project.add_contributor("DevOps Team (Sponsored)")

    my_os_project.add_feature("Advanced caching mechanism", "Charlie (Sponsored Dev)")
    my_os_project.fix_bug("Critical security vulnerability in API", "DevOps Team (Sponsored)")
    # Critical fixes and major features often require dedicated, sustained effort,
    # which financial sponsorship directly enables.
    my_os_project.add_feature("Plugin architecture support", "Charlie (Sponsored Dev)")
    time.sleep(0.5)

    my_os_project.release_new_version()

    print("\n--- Continued Growth ---")
    my_os_project.add_contributor("Eve (New Volunteer)")
    my_os_project.add_feature("Improved error logging", "Eve (New Volunteer)")
    my_os_project.fix_bug("Compatibility issue with Python 3.9", "Alice (Volunteer)")
    time.sleep(0.5)

    my_os_project.release_new_version()

    print("\n--- Simulation End ---")
    print(f"The project '{my_os_project.name}' has evolved from {my_os_project.version.split('.')[0]}.{my_os_project.version.split('.')[1]}.0 to {my_os_project.version}")
    print("This evolution is driven by continuous contributions, often enabled or accelerated by sponsorship.")
