function [uniCorpus, tf_idfn, CosSim, m] = tfidfVec(corpus)

%inputs
%   corpus: DX1 cell vector with D documents
%outputs
%   tfidfn: DXS matrix with each row representing a document and each col
%   representing a string
%   uniCorpus: unique corpus created (aligns with the string
%   representation in tfidfn columns

[tokens, tokens_list, words] = new_tokenizer_2(corpus);


uniCorpus = tokens_list';
uniCorpus = uniCorpus';

%if there are empty fields in the corpus, we must remove
if(ismember(uniCorpus(1), ''))
    uniCorpus = uniCorpus(:,2:end);
end


[n,~] = size(corpus);   %n = number of documents
[~,m] = size(uniCorpus); %m = number of unique words in corpus

tf = zeros(n,m); 
idf = zeros(m,1); 
tf_idfn = zeros(n,m);

[~,N] = cellfun(@size,words,'UniformOutput',false);
N = cell2mat(N);
Nmax = max(N);

words_new = repmat(cellstr(''),n,Nmax);

for k = 1:n
    for j = 1:N(k)
        words_new{k,j} = words{k}{1,j};
    end
end

tic, tf = cell2mat(arrayfun(@(x) sum(strcmp(words_new,uniCorpus(x)),2),1:numel(uniCorpus),'un',0)); toc
toc


idf = log(n./(sum(tf,1)));
idf = diag(idf);

tf_idf = reallog(tf+1)*idf;

for k = 1 : n
    if norm(tf_idf(k,:)) ~= 0       %if norm is 0 the entry is null
        tf_idfn(k,:) = tf_idf(k,:)/norm(tf_idf(k,:));
    else
        tf_idfn(k,:) = 0;
    end
end

tf_idfn = tf_idfn';

CosSim = tf_idfn'*tf_idfn;

end
