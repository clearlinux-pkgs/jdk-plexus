Name     : jdk-plexus
Version  : 3.3.1 
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/3.3.1/plexus-3.3.1.pom
Source0  : http://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/3.3.1/plexus-3.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : openjdk-dev
BuildRequires : javapackages-tools
BuildRequires : python3
BuildRequires : six
BuildRequires : lxml

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms/plexus
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java/plexus

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/plexus/plexus.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/plexus.xml \
%{buildroot}/usr/share/maven-poms/plexus/plexus.pom \
%{buildroot}/usr/share/java/plexus/plexus.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/plexus.xml
/usr/share/maven-poms/plexus/plexus.pom
