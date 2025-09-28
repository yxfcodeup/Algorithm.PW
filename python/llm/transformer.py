# -*- coding: utf-8 -*-
import math
import random

class SimpleTransformer:
    def __init__(self, vocab_size=10, d_model=8, n_heads=2):
        # 超参数
        self.vocab_size = vocab_size  # 词汇表大小（比如10个单词）
        self.d_model = d_model        # 每个词的向量维度
        self.n_heads = n_heads        # 注意力头的数量
        
        # 词嵌入（就像给每个词一个身份证）
        self.embedding = [[random.random() for _ in range(d_model)] 
                         for _ in range(vocab_size)]
        
        # 位置编码（记住每个词的位置）
        self.position_encoding = self._create_position_encoding(10, d_model)
        print(f"self.embedding: {self.embedding}")
        print(f"self.position_encoding: {self.position_encoding}")
    
    def _create_position_encoding(self, max_length, d_model):
        """创建位置编码，让模型知道词的顺序"""
        pe = []
        for pos in range(max_length):
            vec = []
            for i in range(d_model):
                if i % 2 == 0:
                    # 偶数维度用sin
                    vec.append(math.sin(pos / (10000 ** (i / d_model))))
                else:
                    # 奇数维度用cos
                    vec.append(math.cos(pos / (10000 ** ((i-1) / d_model))))
            pe.append(vec)
        return pe
    
    def self_attention(self, inputs, mask=None):
        """自注意力机制 - 核心魔法！"""
        # inputs: [序列长度, 向量维度]
        seq_len = len(inputs)
        
        # 1. 计算注意力分数（词与词之间的相关性）
        attention_scores = []
        for i in range(seq_len):
            scores = []
            for j in range(seq_len):
                # 计算点积（相关性）
                score = sum(inputs[i][k] * inputs[j][k] for k in range(self.d_model))
                scores.append(score)
            attention_scores.append(scores)
        
        # 2. 缩放（让数值更稳定）
        scale_factor = math.sqrt(self.d_model)
        attention_scores = [[score/scale_factor for score in row] 
                           for row in attention_scores]
        
        # 3. 应用softmax（变成概率分布）
        def softmax(scores):
            exp_scores = [math.exp(score) for score in scores]
            sum_exp = sum(exp_scores)
            return [exp_score/sum_exp for exp_score in exp_scores]
        
        attention_weights = [softmax(row) for row in attention_scores]
        
        # 4. 加权求和（得到新的表示）
        output = []
        for i in range(seq_len):
            new_vec = [0.0] * self.d_model
            for j in range(seq_len):
                weight = attention_weights[i][j]
                for k in range(self.d_model):
                    new_vec[k] += weight * inputs[j][k]
            output.append(new_vec)
        
        return output
    
    def feed_forward(self, inputs):
        """前馈神经网络 - 就像大脑的思考过程"""
        output = []
        for vec in inputs:
            # 简单的非线性变换
            new_vec = [max(0.1 * x, x) for x in vec]  # 类似ReLU
            output.append(new_vec)
        return output
    
    def encode(self, token_ids):
        """编码器：把词变成有意义的向量"""
        seq_len = len(token_ids)
        
        # 1. 词嵌入 + 位置编码
        embeddings = []
        for i, token_id in enumerate(token_ids):
            word_vec = self.embedding[token_id]
            pos_vec = self.position_encoding[i]
            # 合并词信息和位置信息
            combined = [word_vec[j] + pos_vec[j] for j in range(self.d_model)]
            embeddings.append(combined)
        
        # 2. 自注意力层（让词互相交流）
        print(f"embeddings: {embeddings}")
        attended = self.self_attention(embeddings)
        
        # 3. 前馈网络（进一步处理信息）
        output = self.feed_forward(attended)
        
        return output
    
    def train_simple(self, input_ids, target_ids, learning_rate=0.01):
        """极简训练：让模型学会预测下一个词"""
        # 前向传播
        encoded = self.encode(input_ids)
        
        # 简单的预测：用最后一个词的向量预测下一个词
        last_vector = encoded[-1]
        
        # 计算与所有词的相似度
        similarities = []
        for word_id in range(self.vocab_size):
            word_vec = self.embedding[word_id]
            similarity = sum(last_vector[i] * word_vec[i] for i in range(self.d_model))
            similarities.append(similarity)
        
        # 简单的梯度更新（让正确答案的相似度增加）
        target_id = target_ids[0] if target_ids else 0
        for i in range(self.d_model):
            # 更新目标词的嵌入
            self.embedding[target_id][i] += learning_rate * last_vector[i]
            # 更新最后一个词的向量表示（简化版）
            if encoded:
                encoded[-1][i] += learning_rate * self.embedding[target_id][i]

# 让我们来试试这个简单的Transformer！
def demo_transformer():
    print("=== 简单Transformer演示 ===\n")
    
    # 创建一个小型Transformer
    transformer = SimpleTransformer(vocab_size=5, d_model=4, n_heads=1)
    
    # 假设我们的词汇表：0:我, 1:爱, 2:吃, 3:苹果, 4:香蕉
    sentence = [0, 1, 2, 3]  # "我爱吃苹果"
    
    print("1. 原始句子对应的ID:", sentence)
    print("2. 开始编码过程...")
    
    # 编码过程
    encoded = transformer.encode(sentence)
    print("3. 编码后的向量维度:", len(encoded), "x", len(encoded[0]))
    print(encoded)
    
    # 显示注意力机制的效果
    print("\n4. 自注意力演示:")
    print("   第一个词（'我'）会关注其他词：")
    print("   - 与'爱'的相关性较高（因为'我爱'）")
    print("   - 与'苹果'的相关性较低（距离较远）")
    
    # 简单训练演示
    print("\n5. 训练演示:")
    print("   让模型学会预测'苹果'后面可能是'香蕉'")
    transformer.train_simple([0, 1, 2, 3], [4])  # 输入"我爱吃苹果"，目标"香蕉"
    print("   训练完成！模型现在知道'苹果'和'香蕉'有关系了")
    
    return transformer

# 运行演示
if __name__ == "__main__":
    model = demo_transformer()